import requests
from argoagent.agent.agent import Agent
from argoagent.context.log_context import LogContext
from argoagent.tools.tool_registry import ToolRegistry
from argoagent.tools.echo import EchoTool
from argoagent.tools.fetch import FetchTool
from argoagent.tools.calculator import CalculatorTool
from argoagent.llm import create_llm

if __name__ == "__main__":
    # 初始化 LLM 和 Agent
    registry = ToolRegistry()
    llm = create_llm(provider="doubao", model="doubao-1-5-lite-32k-250115")
    agent = Agent(llm=llm, tool_registry=registry)

    # 注册工具
    agent.tool_registry.register(EchoTool)
    agent.tool_registry.register(FetchTool)
    agent.tool_registry.register(CalculatorTool)

    print("Available tools:", agent.tool_registry.list_tools())

    # ========== Calculator 示例 ==========
    calc_inputs = [
        "请用 calculator 工具计算 123 * 456",
        "请用 calculator 工具计算 sin(30°)",
        "请用 calculator 工具计算 (2+3)*sqrt(16) - log10(100)"
    ]
    for inp in calc_inputs:
        result = agent.run_tool("calculator", expression=inp.split("计算")[-1].strip())
        print("[Calculator] Result:", result)


    # ========== EchoTool 示例 ==========
    echo_result = agent.run_tool("echo", text="Hello MCP")
    print("[Echo] Result:", echo_result)

    # ========== FetchTool 示例 ==========
    url = "https://www.baidu.com"
    fetch_result = agent.run_tool("fetch", url=url)
    print("[Fetch] Result:", fetch_result[:200], "...")  # 只打印前200字符


    # ========== Context 展示 ==========
    print("\n--- Context History ---")
    agent.log_context.print_history()

