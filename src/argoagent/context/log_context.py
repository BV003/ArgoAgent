import os
from datetime import datetime

class LogContext:
    """简单上下文存储"""
    def __init__(self):
        self.history = []

    def add_message(self, role, content):
        self.history.append({"role": role, "content": content})
    
    def print_history(self):
        """打印历史到控制台"""
        print("\n**打印对话历史**")
        for i, msg in enumerate(self.history, 1):
            print(f" {msg['role']}: {msg['content']}")
        print("=====================")

    def save_to_file(self, log_dir="logs"):
        """保存历史到日志文件（按日期区分）"""
        # 确保日志目录存在
        os.makedirs(log_dir, exist_ok=True)
        date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join(log_dir, f"{date_str}_chat.log")

        with open(filename, "a", encoding="utf-8") as f:
            f.write("\n**打印对话历史**\n")
            for msg in self.history:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{timestamp}] {msg['role']}: {msg['content']}\n")
            
            f.write("=" * 40 + "\n")  # 分隔符，表示一次会话结束