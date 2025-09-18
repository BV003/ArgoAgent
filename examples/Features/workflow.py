from argoagent.agent.agent import Agent
from argoagent.context.context import Context
from argoagent.tools.registry import ToolRegistry
from argoagent.tools.builtins.echo import EchoTool 
from argoagent.tools.builtins.fetch import FetchTool
from argoagent.llm import create_llm
from argoagent.workflows.loop import LoopWorkflow
from argoagent.workflows.human_in_loop import HumanInLoopWorkflow

if __name__ == "__main__":
    
    llm = create_llm(provider="doubao", model="doubao-1-5-lite-32k-250115")
    
    # 初始化 Agent，挂上 LLM
    agent = Agent(llm=llm)
    
    # 注册工具
    agent.registry.register(EchoTool)
    agent.registry.register(FetchTool)



    loop_workflow = LoopWorkflow(agent, max_steps=5)
    result = loop_workflow.run("请使用 echo 工具和 fetch 工具，最后用 echo 工具输出百度首页的标题关键词")
    print("循环工作流结果:", result)

    # 方式2: 使用人机交互工作流
    human_workflow = HumanInLoopWorkflow(agent, max_steps=3)
    result = human_workflow.run("请计算123乘以456的结果")
    print("人机交互工作流结果:", result)
    
    # ========== 打印上下文 ==========
    print("\n--- Context History ---")
    for msg in agent.context.get_history():
        print(f"{msg['role']}: {msg['content']}")
