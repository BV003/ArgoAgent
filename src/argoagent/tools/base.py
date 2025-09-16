class Tool:
    name: str = "base_tool"
    description: str = "Base tool"

    def run(self, **kwargs):
        raise NotImplementedError
