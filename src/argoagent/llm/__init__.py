# 从子模块导出核心类，供外部直接使用
from .base_llm import BaseLLM
from .openai_llm import OpenAILLM
from .doubao_llm import DouBaoLLM

# 工厂函数：统一创建LLM实例的入口
def create_llm(provider: str = "openai", **kwargs) -> BaseLLM:
    """
    创建LLM实例的工厂函数
    
    Args:
        provider: LLM提供商，支持"openai"和"doubao"
       ** kwargs: 传递给具体LLM类的参数（如model、temperature等）
        
    Returns:
        BaseLLM实例
        
    Raises:
        ValueError: 当provider不被支持时
    """
    provider = provider.lower()  # 统一转为小写，避免大小写问题
    if provider == "openai":
        return OpenAILLM(**kwargs)
    elif provider == "doubao":
        return DouBaoLLM(** kwargs)
    else:
        raise ValueError(
            f"不支持的LLM提供商: {provider}，当前支持的有：['openai', 'doubao']"
        )

# 声明包的公开接口（明确哪些可以被外部导入）
__all__ = ["BaseLLM", "OpenAILLM", "DouBaoLLM", "create_llm"]
    