from typing import List, Dict, Any  # 新增这行导入

class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register(self, tool_cls):
        tool = tool_cls()
        self.tools[tool.name] = tool

    def get(self, name):
        return self.tools.get(name)

    # def list_tools(self):
    #     return list(self.tools.keys())
    
    def list_tools(self) -> List[Dict[str, Any]]:
        tool_list = []
        for tool in self.tools.values():
            # 收集工具的核心信息（假设 BaseTool 定义了这些属性）
            tool_info = {
                "name": tool.name,  # 工具名（如 "echo"）
                "description": tool.description,  # 功能描述（如 "输出指定文本"）
                "parameters": tool.parameters  # 参数要求（如 {"content": "需要输出的文本"}）
            }
            tool_list.append(tool_info)
        return tool_list
