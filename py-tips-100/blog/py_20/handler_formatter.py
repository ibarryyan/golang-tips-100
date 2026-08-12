"""logging handler 和 formatter 演示"""
import logging
import os
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler


def demo_multiple_handlers():
    """多个 Handler：控制台 + 文件"""
    logger = logging.getLogger("multi_handler")
    logger.setLevel(logging.DEBUG)

    # 控制台：INFO 及以上
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
    ))

    # 文件：DEBUG 及以上
    log_file = os.path.join(os.path.dirname(__file__), "app.log")
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    ))

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.debug("这条只进文件")
    logger.info("这条进控制台和文件")
    logger.warning("警告信息")
    logger.error("错误信息")


def demo_rotating_handler():
    """按大小轮转的文件 Handler"""
    logger = logging.getLogger("rotating")
    logger.setLevel(logging.DEBUG)

    log_file = os.path.join(os.path.dirname(__file__), "rotating.log")
    handler = RotatingFileHandler(
        log_file,
        maxBytes=500,  # 500 字节轮转（演示用，实际应设更大）
        backupCount=3,
        encoding="utf-8",
    )
    handler.setFormatter(logging.Formatter(
        "%(asctime)s [%(levelname)s] %(message)s"
    ))
    logger.addHandler(handler)

    for i in range(50):
        logger.info(f"日志条目 {i}: 这是一条测试日志消息")
    print(f"轮转日志已写入: {log_file}")


def demo_formatter_fields():
    """Formatter 常用字段"""
    logger = logging.getLogger("format_demo")
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(filename)s:%(lineno)d | %(funcName)s | %(message)s",
        datefmt="%H:%M:%S",
    ))
    logger.addHandler(handler)

    def my_function():
        logger.info("这条日志包含丰富的上下文信息")

    my_function()


if __name__ == "__main__":
    print("=== 多 Handler ===")
    demo_multiple_handlers()

    print("\n=== 轮转 Handler ===")
    demo_rotating_handler()

    print("\n=== Formatter 字段 ===")
    demo_formatter_fields()
