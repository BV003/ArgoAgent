# workflows/base.py
from abc import ABC, abstractmethod

class BaseWorkflow(ABC):
    """工作流基类，定义统一接口"""
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, *args, **kwargs):
        """执行工作流"""
        raise NotImplementedError
