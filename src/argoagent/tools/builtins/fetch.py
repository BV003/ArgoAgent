from ..base import Tool
import requests

class FetchTool(Tool):
    name = "fetch"
    description = "Fetch content from a URL"

    def run(self, url: str, max_length: int = 3000):
        """
        从指定 URL 获取内容。
        参数:
            url: 要请求的网页地址
            max_length: 限制返回内容长度，避免太长
        """
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            text = response.text
            if len(text) > max_length:
                return text[:max_length] + "..."
            return text
        except Exception as e:
            return f"Error fetching {url}: {str(e)}"

