import os
from openai import OpenAI
from .base_llm import BaseLLM
from dotenv import load_dotenv

load_dotenv()

class DouBaoLLM(BaseLLM):
    def __init__(self, model="doubao-1-5-lite-32k-250115",temperature=0.0, **kwargs):
        self.client = OpenAI(
            base_url=os.getenv("DOUBAO_BASE_URL", "https://ark.cn-beijing.volces.com/api/v3"),
            api_key=os.getenv("ARK_API_KEY"),
        )
        self.model = model

    def generate(self, prompt: str) -> str:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "你是人工智能助手"},
                {"role": "user", "content": prompt},
            ],
        )
        return completion.choices[0].message.content