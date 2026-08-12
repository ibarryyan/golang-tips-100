"""环境变量读取的最佳实践示例"""
import os
from dataclasses import dataclass


@dataclass
class Config:
    """应用配置，从环境变量读取"""
    api_key: str
    db_host: str
    db_port: int
    debug: bool

    @classmethod
    def from_env(cls) -> "Config":
        return cls(
            api_key=os.environ["API_KEY"],  # 必须设置
            db_host=os.environ.get("DB_HOST", "localhost"),
            db_port=int(os.environ.get("DB_PORT", "5432")),
            debug=os.environ.get("DEBUG", "false").lower() == "true",
        )

    def __repr__(self) -> str:
        # 不暴露api_key
        return (
            f"Config(api_key=***, db_host={self.db_host}, "
            f"db_port={self.db_port}, debug={self.debug})"
        )


def demo_basic_env():
    """基础环境变量读取"""
    print("=== 基础读取 ===")
    os.environ["TEST_VAR"] = "hello"

    # 直接读取
    val = os.environ["TEST_VAR"]
    print(f"  直接读取: {val}")

    # 带默认值
    val = os.environ.get("NOT_SET", "default")
    print(f"  带默认值: {val}")

    # 不存在返回None
    val = os.environ.get("ALSO_NOT_SET")
    print(f"  不存在: {val}")

    # 设置
    os.environ["NEW_VAR"] = "value"
    print(f"  设置后: {os.environ['NEW_VAR']}")

    del os.environ["TEST_VAR"]
    del os.environ["NEW_VAR"]


def demo_config_pattern():
    """配置模式"""
    print("\n=== 配置模式 ===")
    # 模拟设置环境变量
    os.environ["API_KEY"] = "sk-test-key-12345"
    os.environ["DB_HOST"] = "192.168.1.100"
    os.environ["DB_PORT"] = "5432"
    os.environ["DEBUG"] = "true"

    try:
        config = Config.from_env()
        print(f"  {config}")
        print(f"  api_key长度: {len(config.api_key)}")
        print(f"  debug模式: {config.debug}")
    except KeyError as e:
        print(f"  缺少必需的环境变量: {e}")
        return

    # 清理
    for key in ["API_KEY", "DB_HOST", "DB_PORT", "DEBUG"]:
        del os.environ[key]


def demo_missing_required():
    """缺少必需变量时的处理"""
    print("\n=== 缺少必需变量 ===")
    # 不设置API_KEY
    os.environ.pop("API_KEY", None)

    try:
        config = Config.from_env()
    except KeyError as e:
        print(f"  正确捕获错误: 缺少 {e}")


def demo_type_conversion():
    """类型转换"""
    print("\n=== 类型转换 ===")
    # 环境变量都是字符串
    os.environ["PORT"] = "8080"
    os.environ["RATIO"] = "0.95"
    os.environ["ENABLED"] = "true"

    # 手动转换
    port = int(os.environ["PORT"])
    ratio = float(os.environ["RATIO"])
    enabled = os.environ["ENABLED"].lower() == "true"

    print(f"  int: {port} ({type(port).__name__})")
    print(f"  float: {ratio} ({type(ratio).__name__})")
    print(f"  bool: {enabled} ({type(enabled).__name__})")

    # 清理
    for key in ["PORT", "RATIO", "ENABLED"]:
        del os.environ[key]


def demo_dotenv_pattern():
    """演示.env模式（不依赖第三方库）"""
    print("\n=== .env文件模式 ===")

    # 模拟.env文件内容
    env_content = """\
API_KEY=sk-from-dotenv
DB_HOST=localhost
DB_PORT=5432
DEBUG=false
"""

    # 手动解析.env文件
    for line in env_content.strip().split("\n"):
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())

    config = Config.from_env()
    print(f"  {config}")

    # 清理
    for key in ["API_KEY", "DB_HOST", "DB_PORT", "DEBUG"]:
        os.environ.pop(key, None)


if __name__ == "__main__":
    demo_basic_env()
    demo_config_pattern()
    demo_missing_required()
    demo_type_conversion()
    demo_dotenv_pattern()
