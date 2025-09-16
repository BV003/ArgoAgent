from ..tools.registry import ToolRegistry

class Agent:
    def __init__(self, name="ArgoAgent"):
        self.name = name
        self.registry = ToolRegistry()

    def run(self, tool_name: str, **kwargs):
        tool = self.registry.get(tool_name)
        if not tool:
            raise ValueError(f"Tool {tool_name} not found")
        return tool.run(**kwargs)
