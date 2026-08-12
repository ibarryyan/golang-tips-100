"""print 调试 vs logging 调试演示"""
import logging
import os


def setup_logger():
    """配置 logger"""
    logger = logging.getLogger("myapp")
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        datefmt="%H:%M:%S",
    ))
    logger.addHandler(handler)
    return logger


# === print 调试：简单但不规范 ===
def process_order_print(order_id):
    print(f"Processing order: {order_id}")
    # ... 业务逻辑
    result = {"status": "ok", "order_id": order_id}
    print(f"Order done: {order_id}")
    return result


# === logging 调试：规范且可控 ===
def process_order_logging(order_id, logger):
    logger.info(f"开始处理订单: {order_id}")
    try:
        # ... 业务逻辑
        logger.debug(f"订单 {order_id} 处理详情: step1=ok, step2=ok")
        logger.info(f"订单处理完成: {order_id}")
        return {"status": "ok", "order_id": order_id}
    except Exception as e:
        # logger.exception 自动附带堆栈信息
        logger.exception(f"订单处理失败: {order_id}")
        raise


def demo_exception_logging():
    """演示异常日志"""
    logger = setup_logger()

    try:
        result = 10 / 0
    except ZeroDivisionError:
        logger.error("除零错误！", exc_info=True)
        # 或者用 logger.exception("除零错误！")


def demo_debug_flag():
    """使用 __debug__ 控制调试输出"""
    # python 运行时 __debug__ = True
    # python -O 运行时 __debug__ = False（assert 和 if __debug__ 被跳过）
    x, y = 42, 99

    if __debug__:
        print(f"[DEBUG] x={x}, y={y}")

    print(f"正常输出: x+y={x + y}")


if __name__ == "__main__":
    print("=== print 调试 ===")
    process_order_print(1001)

    print("\n=== logging 调试 ===")
    logger = setup_logger()
    process_order_logging(1002, logger)

    print("\n=== 异常日志 ===")
    demo_exception_logging()

    print("\n=== __debug__ 标志 ===")
    demo_debug_flag()

    print("\n建议：开发用 print 快速验证，生产用 logging 规范输出")
