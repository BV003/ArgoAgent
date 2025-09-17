from ..base import Tool
import requests

class FetchTool(Tool):
    name = "fetch"
    description = "Fetch content from a URL"
    parameters = {
    "url": "需要抓取的网页地址（必填，字符串类型，必须包含http/https协议）",
    "max_length": "返回内容的最大长度（可选，整数类型，默认值为1000，超出部分会被截断）"
    }

    def run(self, url: str, max_length: int = 1000):
        """
        从指定 URL 获取内容。
        参数:
            url: 要请求的网页地址
            max_length: 限制返回内容长度，避免太长
        """
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            response.encoding = "utf-8" 
            text = response.text
            if len(text) > max_length:
                return text[:max_length] + "..."
            return text
        except Exception as e:
            return f"Error fetching {url}: {str(e)}"

