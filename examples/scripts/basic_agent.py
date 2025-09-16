from argoagent.core.agent import Agent
from argoagent.tools.registry import ToolRegistry
from argoagent.tools.builtins.echo import EchoTool
from argoagent.tools.builtins.fetch import FetchTool
from argoagent.llm import create_llm


if __name__ == "__main__":
    agent = Agent()
    agent.registry.register(EchoTool)
    agent.registry.register(FetchTool)

    print("Available tools:", agent.registry.list_tools())

    # 用工具
    result1 = agent.run("echo", text="Hello MCP")
    print("Result1:", result1)

    # 调用 LLM 
    llm = create_llm(provider="doubao", model="doubao-1-5-lite-32k-250115")
    reply = llm.generate("Say hello to MCP world!")
    print("LLM reply:", reply)
