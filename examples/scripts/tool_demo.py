from argoagent.core.agent import Agent
from argoagent.core.context import Context
from argoagent.tools.registry import ToolRegistry
from argoagent.tools.builtins.echo import EchoTool
from argoagent.tools.builtins.fetch import FetchTool
from argoagent.llm import create_llm


if __name__ == "__main__":
    agent = Agent()
    agent.registry.register(EchoTool)
    agent.registry.register(FetchTool)

    print("Available tools:", agent.registry.list_tools())

    # # echo tool
    # result1 = agent.run("echo", text="Hello MCP")
    # print("Result1:", result1)

    # # 调用 LLM 
    # llm = create_llm(provider="doubao", model="doubao-1-5-lite-32k-250115")
    # reply = llm.generate("Say hello to MCP world!")
    # print("LLM reply:", reply)

    # # 用 FetchTool
    # url = "https://example.com"
    # result2 = agent.run("fetch", url="https://www.baidu.com")
    # print("FetchResult:", result2)
    
    # # 展示 Context 功能
    # ctx = Context()
    # # 记录对话到 context
    # ctx.add_message("user", "Hello MCP")
    # ctx.add_message("agent", result1)
    # ctx.add_message("user", f"Fetch {url}")
    # ctx.add_message("agent", result2)
    # # 查看 context 历史
    # print("\n--- Context History ---")
    # for msg in ctx.get_history():
    #     print(f"{msg['role']}: {msg['content'][:50]}...")  # 只显示前50字符
