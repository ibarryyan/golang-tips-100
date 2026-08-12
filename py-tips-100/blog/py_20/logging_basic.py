"""logging 模块基础配置演示"""
import logging


def demo_basic_config():
    """基础配置"""
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logger = logging.getLogger(__name__)

    logger.debug("调试信息：变量 x=42")
    logger.info("一般信息：用户登录成功")
    logger.warning("警告信息：磁盘空间不足")
    logger.error("错误信息：数据库连接失败")
    logger.critical("严重错误：系统即将崩溃")


def demo_level_filter():
    """日志级别过滤"""
    logger = logging.getLogger("level_demo")

    # 设置为 WARNING，只输出 WARNING 及以上
    handler = logging.StreamHandler()
    handler.setLevel(logging.WARNING)
    handler.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))

    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    print("--- 只输出 WARNING 及以上 ---")
    logger.debug("这条不会显示")
    logger.info("这条也不会显示")
    logger.warning("这条会显示")
    logger.error("这条也会显示")


def demo_logger_usage():
    """在函数中使用 logger"""
    logger = logging.getLogger("myapp.service")

    def process_data(data):
        logger.debug(f"开始处理: data={data}")
        result = data * 2
        logger.debug(f"中间结果: result={result}")
        result = result + 10
        logger.info(f"最终结果: {result}")
        return result

    process_data(21)


if __name__ == "__main__":
    print("=== 基础配置 ===")
    demo_basic_config()

    print("\n=== 级别过滤 ===")
    demo_level_filter()

    print("\n=== 函数中使用 ===")
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
        force=True,  # 覆盖之前的配置
    )
    demo_logger_usage()
