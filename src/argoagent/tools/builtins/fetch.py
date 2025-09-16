from ..base import Tool

class FetchTool(Tool):
    name = "fetch"
    description = "Fake fetch from URL"

    def run(self, url: str):
        return f"Fetched content from {url}"
