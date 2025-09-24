from argoagent.core.agent import Agent
from argoagent.context.context import Context
from argoagent.tools.registry import ToolRegistry
from argoagent.tools.builtins.echo import EchoTool 
from argoagent.tools.builtins.fetch import FetchTool
from argoagent.llm import create_llm

if __name__ == "__main__":
    
    llm = create_llm(provider="doubao", model="doubao-1-5-lite-32k-250115")
    
    # 初始化 Agent，挂上 LLM
    agent = Agent(llm=llm)
    
    # 注册工具
    agent.registry.register(EchoTool)
    agent.registry.register(FetchTool)

    print("Available tools:", agent.registry.list_tools())

    # ========== 示例 1：调用 echo 工具 ==========
    user_input1 = "请用 echo 工具输出一句话"
    result1 = agent.run_single_step(user_input1)
    print("\n[示例 1] Agent result:", result1)

    # ========== 示例 2：调用 fetch 工具 ==========
    user_input2 = "帮我抓取 https://www.baidu.com 的内容"
    result2 = agent.run_single_step(user_input2)
    print("\n[示例 2] Agent result:", result2)


    user_input3 = "请使用 echo 工具和 fetch 工具，最后用 echo 工具输出百度首页的标题关键词"
    result3 = agent.run_loop(user_input3)
    print("\n[示例 3] Agent result:", result3)
    
    # ========== 打印上下文 ==========
    print("\n--- Context History ---")
    for msg in agent.context.get_history():
        print(f"{msg['role']}: {msg['content']}")
