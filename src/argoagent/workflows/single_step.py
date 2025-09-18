from .base import BaseWorkflow
from ..agent.agent import Agent

class SingleStepWorkflow(BaseWorkflow):
    """单步工作流：仅执行一次Agent的单步操作"""
    
    def run(self, user_input: str) -> str:
        """直接调用Agent的单步处理方法"""
        return self.agent.run_single_step(user_input)