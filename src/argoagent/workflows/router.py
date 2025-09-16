# workflows/router.py
from .base import BaseWorkflow

class RouterWorkflow(BaseWorkflow):
    """根据条件把任务分发到不同子代理或工具"""
    def __init__(self, name="router_workflow", routing_table=None):
        super().__init__(name)
        self.routing_table = routing_table or {}  # {'task_name': handler}

    def register(self, task_name: str, handler):
        """注册任务和对应处理函数"""
        self.routing_table[task_name] = handler

    def run(self, task_name: str, *args, **kwargs):
        """根据 task_name 找到 handler 并执行"""
        if task_name not in self.routing_table:
            raise ValueError(f"No handler registered for task: {task_name}")
        handler = self.routing_table[task_name]
        return handler(*args, **kwargs)
