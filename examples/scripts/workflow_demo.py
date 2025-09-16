from argoagent.workflows.parallel import ParallelWorkflow
from argoagent.workflows.router import RouterWorkflow

# 并行执行示例
def task1(): return "Result of task1"
def task2(): return "Result of task2"

parallel = ParallelWorkflow()
results = parallel.run([task1, task2])
print("Parallel results:", results)

# 路由执行示例
router = RouterWorkflow()
router.register("say_hello", lambda name: f"Hello {name}")
router.register("say_bye", lambda name: f"Bye {name}")

print(router.run("say_hello", "MCP"))
print(router.run("say_bye", "MCP"))
