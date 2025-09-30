from argoagent.agent.agent import Agent
from argoagent.context.log_context import LogContext
from argoagent.tools.tool_registry import ToolRegistry
from argoagent.tools.echo import EchoTool
from argoagent.tools.fetch import FetchTool
from argoagent.llm import create_llm
from argoagent.workflows.loop import LoopWorkflow
from argoagent.workflows.human_in_loop import HumanInLoopWorkflow
from argoagent.workflows.parallel import ParallelWorkflow
from argoagent.workflows.router import RouterWorkflow

if __name__ == "__main__":
    # ===== 初始化 LLM 和 Agent =====
    llm = create_llm(provider="doubao", model="doubao-1-5-lite-32k-250115")
    agent = Agent(llm=llm)

    # ===== 注册工具 =====
    agent.tool_registry.register(EchoTool)
    agent.tool_registry.register(FetchTool)
    print("Available tools:", agent.tool_registry.list_tools())

    # ===== 循环工作流示例 =====
    loop_workflow = LoopWorkflow(agent, max_steps=5)
    loop_result = loop_workflow.run(
        "请使用 echo 工具和 fetch 工具，最后用 echo 工具输出百度首页的标题关键词"
    )
    print("\n[LoopWorkflow] Result:", loop_result)

    # ===== 人机交互工作流示例 =====
    human_workflow = HumanInLoopWorkflow(agent, max_steps=3)
    human_result = human_workflow.run("请计算123乘以456的结果")
    print("\n[HumanInLoopWorkflow] Result:", human_result)

    # ===== 并行工作流示例 =====
    def task1(): return "Result of task1"
    def task2(): return "Result of task2"

    parallel = ParallelWorkflow()
    parallel_results = parallel.run([task1, task2])
    print("\n[ParallelWorkflow] Results:", parallel_results)

    # ===== 路由工作流示例 =====
    router = RouterWorkflow()
    router.register("say_hello", lambda name: f"Hello {name}")
    router.register("say_bye", lambda name: f"Bye {name}")

    print("\n[RouterWorkflow] say_hello:", router.run("say_hello", "MCP"))
    print("[RouterWorkflow] say_bye:", router.run("say_bye", "MCP"))

    # ===== 打印上下文 =====
    agent.log_context.print_history()
