import math
import re
from .base import Tool  
 

class CalculatorTool(Tool):
    name="calculator"
    description="执行数学计算，支持加减乘除、幂运算、三角函数等表达式"
    parameters={
        "expression": "字符串，需要计算的数学表达式，例如 '123*456'、'sin(30°)'、'sqrt(16)'"
    }
    
    def run(self, expression: str) -> str:
        """
        计算数学表达式并返回结果
        
        支持的运算符和函数：
        - 基础运算：+、-、*、/、//（整除）、%（取余）、**（幂运算）
        - 函数：sin、cos、tan、log、log10、sqrt、abs、round
        - 常量：pi（π）、e（自然常数）
        - 角度转换：支持在数字后加°表示角度（如 30° 会自动转换为弧度）
        """
        try:
            # 替换角度符号（如 30° → math.radians(30)）
            expression = re.sub(r'(-?\d+(\.\d+)?)°', r'math.radians(\1)', expression)

            
            # 允许的安全函数和常量（限制执行范围，避免安全风险）
            safe_globals = {
                'math': math,
                'pi': math.pi,
                'e': math.e,
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan,
                'log': math.log,
                'log10': math.log10,
                'sqrt': math.sqrt,
                'abs': abs,
                'round': round
            }
            
            # 执行计算（使用eval但限制作用域，比直接eval更安全）
            result = eval(expression, {"__builtins__": None}, safe_globals)
            
            # 格式化结果（避免科学计数法）
            if isinstance(result, float):
                # 小数位不超过6位，且去除末尾的0
                return f"{result:.6f}".rstrip('0').rstrip('.') if '.' in f"{result:.6f}" else f"{int(result)}"
            return str(result)
        
        except Exception as e:
            return f"计算失败：{str(e)}，请检查表达式格式（例如 '123*456'、'sqrt(16)'）"


