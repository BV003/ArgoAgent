from typing import Dict


class Tool:
    name: str = "base_tool"
    description: str = "Base tool"
    parameters: Dict[str, str] = {}  # 参数名和说明

    def run(self, **kwargs):
        raise NotImplementedError
