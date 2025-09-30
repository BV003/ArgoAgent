from .base import Tool

class EchoTool(Tool):
    name = "echo"
    description = "Echo input text"
    parameters = {
        "text": "需要输出的文本内容（必填，字符串类型）"
    }
    
    def run(self, text: str):
        return f"EchoTool: {text}"
