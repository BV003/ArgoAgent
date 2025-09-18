from .base import BaseWorkflow
from ..agent.agent import Agent

class HumanInLoopWorkflow(BaseWorkflow):
    """人机交互工作流：关键步骤需要人工确认"""
    
    def __init__(self, agent: Agent, max_steps: int = 5):
        super().__init__(agent)
        self.max_steps = max_steps
    
    def run(self, user_input: str) -> str:
        current_step = 0
        last_result = ""
        
        while current_step < self.max_steps:
            # 1. 执行单步操作
            last_result = self.agent.run_single_step(user_input)
            
            # 2. 检查是否需要终止
            if "任务已完成" in last_result:
                break
                
            # 3. 询问用户是否继续
            user_confirm = input(f"当前结果：{last_result}\n是否继续？(y/n) ")
            if user_confirm.lower() != 'y':
                last_result += "\n用户已终止操作"
                break
                
            # 4. 准备下一步
            user_input = last_result
            current_step += 1
            
        return last_result