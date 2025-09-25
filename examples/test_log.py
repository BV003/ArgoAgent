# test_log.py
from argoagent.context.log_context import LogContext
import os

def main():
    # 创建日志上下文
    log = LogContext()

    # 添加一些消息
    log.add_message("User", "你好")
    log.add_message("Assistant", "你好，有什么可以帮你？")
    log.add_message("User", "帮我写一个测试脚本")
    log.add_message("Assistant", "好的，已经写好啦！")

    # 打印历史
    log.print_history()

    # 保存日志文件

    log.save_to_file()


if __name__ == "__main__":
    main()
