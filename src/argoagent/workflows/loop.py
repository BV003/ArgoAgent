from .base import BaseWorkflow
from ..agent.agent import Agent

class LoopWorkflow(BaseWorkflow):
    """循环工作流：多轮执行直到完成任务或达到最大步数"""
    
    def __init__(self, agent: Agent, max_steps: int = 5):
        super().__init__(agent)
        self.max_steps = max_steps  # 最大步数，防止无限循环
    
    def run(self, user_input: str) -> str:
        current_step = 0
        last_result = ""
        
        while current_step < self.max_steps:
            last_result = self.agent.run_single_step(user_input)
            
            # 检查终止条件
            if self._check_termination(last_result):
                break
                
            # 准备下一步输入（用上一步结果作为输入）
            user_input = last_result
            current_step += 1
            
            # 最后一步仍未完成，提示用户
            if current_step == self.max_steps:
                last_result += "\n已达到最大步骤限制，若需继续请重新输入指令。"
                
        return last_result
    
    def _check_termination(self, result: str) -> bool:
        """检查是否需要终止循环"""
        # 1. 任务完成关键词
        if "任务已完成" in result:
            return True
            
        # 2. 错误状态
        if "工具调用失败" in result and "未找到" in result:
            return True
            
        # 3. 可以添加更多自定义终止条件
        return False