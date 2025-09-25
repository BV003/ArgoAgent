from bs4 import BeautifulSoup  # 需要安装 beautifulsoup4（pip install beautifulsoup4）
from ..base import Tool  
 
class HTMLParserTool(Tool):
    name = "html_parser"
    description = "从HTML文本中提取指定标签的内容（如标题、链接、段落等）"
    parameters = {
        "html": "字符串，需要解析的HTML文本",
        "tag": "字符串，要提取的HTML标签（如 'title'、'a'、'p'）",
        "attr": "字符串，可选，标签的属性（如提取链接时用 'href'）"
    }

    def run(self, html: str, tag: str, attr: str = None) -> str:
        """
        解析HTML并提取指定标签的内容或属性
        
        示例：
        - 提取标题：html_parser(html, tag='title') → 返回 <title>标签内的文本
        - 提取所有链接：html_parser(html, tag='a', attr='href') → 返回所有<a>标签的href属性
        """
        try:
            soup = BeautifulSoup(html, 'html.parser')
            elements = soup.find_all(tag)

            if not elements:
                return f"未找到标签 <{tag}>"

            result = []
            for i, elem in enumerate(elements, 1):
                if attr:
                    # 提取标签的属性值（如 href、src）
                    value = elem.get(attr, f"[{tag}标签无 {attr} 属性]")
                    result.append(f"{i}. <{tag} {attr}='{value}'>")
                else:
                    # 提取标签内的文本（去除多余空格）
                    text = ' '.join(elem.get_text().split())
                    result.append(f"{i}. <{tag}> {text}")

            return "\n".join(result)

        except Exception as e:
            return f"解析失败：{str(e)}"
