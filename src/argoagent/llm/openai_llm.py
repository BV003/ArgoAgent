import os
import openai
from .base_llm import BaseLLM
from dotenv import load_dotenv

load_dotenv()  # load .env if exists

class OpenAILLM(BaseLLM):
    def __init__(self, model="gpt-4o-mini", temperature=0.0):
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