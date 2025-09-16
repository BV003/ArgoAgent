class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register(self, tool_cls):
        tool = tool_cls()
        self.tools[tool.name] = tool

    def get(self, name):
        return self.tools.get(name)

    def list_tools(self):
        return list(self.tools.keys())
