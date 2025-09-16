import os
from abc import ABC, abstractmethod
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class BaseLLM(ABC):
    """LLM调用的抽象基类，定义统一接口"""
    @abstractmethod
    def generate(self, prompt: str) -> str:
        """生成模型响应"""
        raise NotImplementedError

class DouBaoLLM(BaseLLM):
    """豆包LLM实现"""
    def __init__(self, model="doubao-1-5-lite-32k-250115", temperature=0.0, **kwargs):
        # 导入OpenAI客户端（用于调用豆包API）
        from openai import OpenAI
        
        self.client = OpenAI(
            base_url=os.getenv("DOUBAO_BASE_URL", "https://ark.cn-beijing.volces.com/api/v3"),
            api_key=os.getenv("ARK_API_KEY"),
        )
        self.model = model
        self.temperature = temperature

    def generate(self, prompt: str) -> str:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "你是人工智能助手"},
                {"role": "user", "content": prompt},
            ],
            temperature=self.temperature,
        )
        return completion.choices[0].message.content

class OpenAILLM(BaseLLM):
    """OpenAI LLM实现"""
    def __init__(self, model="gpt-4o-mini", temperature=0.0):
        # 导入OpenAI库
        import openai
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not set in env or .env")
        
        openai.api_key = api_key
        self.model = model
        self.temperature = temperature

    def generate(self, prompt: str) -> str:
        resp = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
        )
        return resp["choices"][0]["message"]["content"].strip()

# 方便外部调用的工厂函数
def create_llm(provider: str = "openai",** kwargs) -> BaseLLM:
    """
    创建LLM实例的工厂函数
    
    Args:
        provider: LLM提供商，支持"openai"和"doubao"
        **kwargs: 传递给具体LLM类的参数
        
    Returns:
        BaseLLM实例
    """
    if provider.lower() == "openai":
        return OpenAILLM(** kwargs)
    elif provider.lower() == "doubao":
        return DouBaoLLM(**kwargs)
    else:
        raise ValueError(f"不支持的LLM提供商: {provider}")
