from src.argoagent.core.agent import Agent
from src.argoagent.tools.registry import ToolRegistry
from src.argoagent.tools.builtins.filesystem import EchoTool
from src.argoagent.tools.builtins.fetch import FetchTool
from src.argoagent.core.llm import create_llm

if __name__ == "__main__":
    agent = Agent()
    agent.registry.register(EchoTool)
    agent.registry.register(FetchTool)

    print("Available tools:", agent.registry.list_tools())

    # 用工具
    result1 = agent.run("echo", text="Hello MCP")
    print("Result1:", result1)

    # 调用 LLM (用OpenAI)
    llm = create_llm(provider="openai", model="gpt-4o-mini")
    reply = llm.generate("Say hello to MCP world!")
    print("LLM reply:", reply)
