# workflows/parallel.py
from .base import BaseWorkflow
from concurrent.futures import ThreadPoolExecutor, as_completed

class ParallelWorkflow(BaseWorkflow):
    """并行执行多个任务"""
    def __init__(self, name="parallel_workflow"):
        super().__init__(name)

    def run(self, tasks: list):
        """
        tasks: 一个列表，每个元素是一个可调用对象 (function)
        返回值：任务结果列表，顺序与输入一致
        """
        results = []
        with ThreadPoolExecutor() as executor:
            future_to_task = {executor.submit(task): task for task in tasks}
            for future in as_completed(future_to_task):
                try:
                    results.append(future.result())
                except Exception as e:
                    results.append({"error": str(e)})
        return results
