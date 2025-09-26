from ..tools.registry import ToolRegistry
from typing import Dict, Any, Optional, List 
from ..context.log_context import LogContext          
import json
import re

class Agent:
    def __init__(self, name="ArgoAgent", llm=None, log_context=None, retrieved_context="", tool_registry=None):
        self.name = name
        self.llm = llm
        self.log_context = log_context
        self.retrieved_context = retrieved_context
        self.tool_registry = tool_registry 

        
    # 执行工具
    def run(self, tool_name: str, **kwargs):
        tool = self.tool_registry.get(tool_name)
        if not tool:
            raise ValueError(f"Tool {tool_name} not found")
        return tool.run(**kwargs)
    
    # 解析 LLM 输出
    def parse_llm_response(self, llm_output: str) -> Dict[str, Any]:
        """解析 LLM 输出，提取工具调用信息，确保返回包含 action 字段的字典"""
        # -------------------------- 新增：输出清理步骤 --------------------------
        # 1. 去除前后空格和换行（避免首尾多余字符）
        clean_output = llm_output.strip()
        
        # 2. 提取纯 JSON 片段（剔除 "任务已完成" 等多余文本）
        # 正则匹配：从第一个 { 开始，到最后一个 } 结束（支持多行 JSON）

        json_match = re.search(r'\{[\s\S]*\}', clean_output)  # [\s\S]* 匹配任意字符（包括换行）
        if json_match:
            json_str = json_match.group(0)  # 只保留 JSON 部分
        else:
            # 无 JSON 时，视为直接回答
            return {
                "action": "direct_response",
                "content": clean_output,
                "error": "未检测到 JSON 格式，视为直接回答"
            }
        
        # 3. 替换全角符号为半角（JSON 只支持半角逗号、引号等）
        full_to_half = {
            '，': ',',  # 全角逗号 → 半角逗号（当前报错的核心原因）
            '。': '.',
            '：': ':',
            '；': ';',
            '“': '"',
            '”': '"',
            '‘': "'",
            '’': "'"
        }
        for full, half in full_to_half.items():
            json_str = json_str.replace(full, half)
        try:
            # 优先使用 json 解析（比 eval 更安全）
            parsed = json.loads(json_str)
        except json.JSONDecodeError:
            # 尝试兼容 eval 格式（仅临时过渡用，建议最终统一为 JSON）
            try:
                parsed = eval(json_str)
            except Exception as e:
                # 解析失败时，明确返回 action: error
                return {
                    "action": "error",
                    "content": f"解析失败：{str(e)}，原始输出：{llm_output}"
                }

        # 统一处理：确保所有分支都返回包含 action 的字典
        if isinstance(parsed, dict) and parsed.get("action") == "call_tool" and "name" in parsed:
            # 工具调用场景：返回 action 和工具信息
            return {
                "action": "call_tool",  # 明确包含 action 字段
                "tool_name": parsed["name"],
                "parameters": parsed.get("parameters", {})
            }
        else:
            # 非工具调用场景：返回 action: direct_response
            return {
                "action": "direct_response",  # 明确包含 action 字段
                "content": llm_output if isinstance(parsed, str) else str(parsed)
            }

    
    # 单步调用
    def run_single_step(self, user_input: str) -> str:
        """单步调用：处理一次用户输入，返回结果（对应开源项目的原子操作）"""
        # 1. 记录用户输入到上下文
        self.log_context.add_message(role="user", content=user_input)
        
        # 2. 构造 LLM 提示：包含上下文和工具元信息
        prompt = (
            f"上下文：{self.log_context.get_history()}\n"
            f"可用工具：{self.tool_registry.list_tools()}\n"
            "请根据以下以下规则处理：\n"
            "若需调用工具，输出格式：{'action': 'call_tool', 'name': '工具名', 'parameters': {...}}\n"
            "若无需调用工具，直接输出回答内容\n"
            "当任务完全完成时，请回答任务已完成，无需进一步操作。"
        )
        
        # 3. 调用 LLM 生成决策
        llm_response = self.llm.generate(prompt)
        self.log_context.add_message(role="llm", content=llm_response)
        
        # 4. 解析决策并执行
        parsed = self.parse_llm_response(llm_response)
        if parsed["action"] == "call_tool":
            # 调用工具并记录结果
            try:
                result = self.run(tool_name=parsed["tool_name"],** parsed["parameters"])
                self.log_context.add_message(
                    role="tool",
                    content=f"工具 {parsed['tool_name']} 返回：{result}"
                )
                return result
            except Exception as e:
                error_msg = f"工具调用失败：{str(e)}"
                self.log_context.add_message(role="agent", content=error_msg)
                return error_msg
        elif parsed["action"] == "direct_response":
            # 直接返回 LLM 回答
            self.log_context.add_message(role="llm", content=parsed["content"])
            return parsed["content"]
        else:
            # 处理解析错误
            self.log_context.add_message(role="agent", content=parsed["content"])
            return parsed["content"]
