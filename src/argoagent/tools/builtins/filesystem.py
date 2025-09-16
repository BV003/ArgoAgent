from ..base import Tool

class EchoTool(Tool):
    name = "echo"
    description = "Echo input text"

    def run(self, text: str):
        return f"EchoTool: {text}"
