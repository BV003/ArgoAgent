# workflows/base.py
from abc import ABC, abstractmethod
from ..agent.agent import Agent

class BaseWorkflow(ABC):
    """工作流基类，定义所有工作流的统一接口"""
    
    def __init__(self, agent: Agent):
        self.agent = agent  # 持有Agent实例，复用其核心能力
    
    @abstractmethod
    def run(self, user_input: str) -> str:
        """运行工作流，处理用户输入并返回最终结果"""
        pass