"""API Key安全管理与环境变量注入示例"""
import os
import logging
from typing import Optional

logging.basicConfig(level=logging.INFO, format="  %(message)s")
logger = logging.getLogger(__name__)


class APIKeyManager:
    """API Key安全管理"""

    _SENSITIVE_KEYS = {"api_key", "apikey", "secret", "token", "password"}

    @staticmethod
    def get_key(name: str, required: bool = True) -> Optional[str]:
        """从环境变量安全获取API Key"""
        key = os.environ.get(name)
        if required and not key:
            raise EnvironmentError(
                f"缺少必需的环境变量: {name}。"
                f"请在环境变量或.env文件中设置。"
            )
        return key

    @staticmethod
    def mask(key: str) -> str:
        """脱敏显示"""
        if not key or len(key) <= 8:
            return "***"
        return f"{key[:4]}...{key[-4:]}"

    @staticmethod
    def sanitize_log(data: dict) -> dict:
        """日志脱敏"""
        result = {}
        for k, v in data.items():
            if k.lower() in APIKeyManager._SENSITIVE_KEYS and isinstance(v, str):
                result[k] = APIKeyManager.mask(v)
            else:
                result[k] = v
        return result


class SecretConfig:
    """密钥配置管理"""

    @staticmethod
    def load() -> dict:
        """加载所有密钥配置"""
        return {
            "api_key": os.environ.get("OPENAI_API_KEY"),
            "base_url": os.environ.get("LLM_BASE_URL"),
            "db_url": os.environ.get("DATABASE_URL"),
            "redis_url": os.environ.get("REDIS_URL"),
        }

    @staticmethod
    def validate() -> list[str]:
        """验证必需的密钥是否配置"""
        required = ["OPENAI_API_KEY"]
        missing = [k for k in required if not os.environ.get(k)]
        return missing

    @staticmethod
    def safe_repr() -> dict:
        """安全展示配置（用于日志）"""
        cfg = SecretConfig.load()
        return {
            k: (v[:4] + "..." + v[-4:] if v and len(v) > 8 else "***")
            for k, v in cfg.items()
        }


def demo_masking():
    """脱敏演示"""
    print("=== API Key脱敏 ===")
    keys = [
        "sk-proj-abcdefgh1234567890",
        "sk-short",
        "",
        None,
    ]
    for key in keys:
        masked = APIKeyManager.mask(key) if key else "***"
        print(f"  原始({key!r:.30}) -> 脱敏({masked})")


def demo_log_sanitization():
    """日志脱敏"""
    print("\n=== 日志脱敏 ===")
    log_data = {
        "api_key": "sk-proj-1234567890abcdef",
        "user": "alice",
        "password": "secret123",
        "token": "tok_abc123def456ghi789",
        "endpoint": "/v1/chat/completions",
        "model": "gpt-4",
    }
    safe = APIKeyManager.sanitize_log(log_data)
    print("  原始:")
    for k, v in log_data.items():
        print(f"    {k}: {v}")
    print("  脱敏:")
    for k, v in safe.items():
        print(f"    {k}: {v}")


def demo_env_injection():
    """环境变量注入"""
    print("\n=== 环境变量注入 ===")
    # 模拟设置
    os.environ["OPENAI_API_KEY"] = "sk-test-key-12345678"
    os.environ["LLM_BASE_URL"] = "https://api.openai.com/v1"
    os.environ["DATABASE_URL"] = "postgresql://user:pass@localhost:5432/db"

    # 验证
    missing = SecretConfig.validate()
    print(f"  缺少的必需配置: {missing if missing else '无'}")

    # 安全展示
    print(f"  配置（脱敏）: {SecretConfig.safe_repr()}")

    # 获取Key
    key = APIKeyManager.get_key("OPENAI_API_KEY")
    print(f"  获取Key: {APIKeyManager.mask(key)}")

    # 清理
    for k in ["OPENAI_API_KEY", "LLM_BASE_URL", "DATABASE_URL"]:
        os.environ.pop(k, None)


def demo_missing_key():
    """缺少Key时的处理"""
    print("\n=== 缺少Key处理 ===")
    os.environ.pop("OPENAI_API_KEY", None)

    try:
        key = APIKeyManager.get_key("OPENAI_API_KEY", required=True)
    except EnvironmentError as e:
        print(f"  正确捕获: {e}")

    # 非必需时返回None
    key = APIKeyManager.get_key("OPENAI_API_KEY", required=False)
    print(f"  非必需时: {key}")


def demo_gitignore_pattern():
    """展示.gitignore配置"""
    print("\n=== .gitignore配置 ===")
    gitignore_content = """\
# 密钥和配置文件
.env
.env.local
.env.*.local
*.key
*.pem
secrets.json

# Python
__pycache__/
*.pyc
.venv/
dist/
"""
    print(gitignore_content)


if __name__ == "__main__":
    demo_masking()
    demo_log_sanitization()
    demo_env_injection()
    demo_missing_key()
    demo_gitignore_pattern()
