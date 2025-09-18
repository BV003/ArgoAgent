from argoagent.agent.agent import Agent
from argoagent.context.context import Context
from argoagent.tools.registry import ToolRegistry
from argoagent.tools.builtins.echo import EchoTool 
from argoagent.tools.web.fetch import FetchTool
from argoagent.tools.calculator import CalculatorTool
from argoagent.workflows.loop import LoopWorkflow
from argoagent.workflows.human_in_loop import HumanInLoopWorkflow
from argoagent.llm import create_llm
import requests

if __name__ == "__main__":
    
    llm = create_llm(provider="doubao", model="doubao-1-5-lite-32k-250115")
    
    # 初始化 Agent，挂上 LLM
    agent = Agent(llm=llm)
    
    # 注册工具
    # agent.registry.register(CalculatorTool)
    # # 单步调用
    # inputs = [
    #     "请用 calculator 工具计算 123 * 456",
    #     "请用 calculator 工具计算 sin(30°)",
    #     "请用 calculator 工具计算 (2+3)*sqrt(16) - log10(100)"
    # ]
    # for inp in inputs:
    #     result = agent.run_single_step(inp)
    #     print(result)
    
    
    
        
    # ========== 打印上下文 ==========
    print("\n--- Context History ---")
    for msg in agent.context.get_history():
        print(f"{msg['role']}: {msg['content']}")
