"""requests 超时重试与异常处理演示"""
import requests
from requests.exceptions import (
    Timeout,
    ConnectionError,
    HTTPError,
    RequestException,
)
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


def demo_timeout():
    """超时设置"""
    try:
        # timeout=(连接超时, 读取超时)
        response = requests.get(
            "https://httpbin.org/delay/3",
            timeout=(2, 1),  # 读取超时 1s，会超时
        )
        print(response.status_code)
    except Timeout:
        print("请求超时！")


def demo_exception_handling():
    """完整异常处理"""
    try:
        response = requests.get(
            "https://httpbin.org/status/404",
            timeout=10,
        )
        response.raise_for_status()
    except HTTPError as e:
        print(f"HTTP 错误: {e}")
    except ConnectionError:
        print("连接失败")
    except Timeout:
        print("请求超时")
    except RequestException as e:
        print(f"请求异常: {e}")


def demo_retry():
    """自动重试机制"""
    session = requests.Session()

    retry_strategy = Retry(
        total=3,
        backoff_factor=0.5,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "POST"],
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    try:
        # 503 会触发重试
        response = session.get(
            "https://httpbin.org/status/503",
            timeout=5,
        )
        print(f"最终状态码: {response.status_code}")
    except RequestException as e:
        print(f"重试后仍失败: {e}")


if __name__ == "__main__":
    print("=== 超时 ===")
    demo_timeout()

    print("\n=== 异常处理 ===")
    demo_exception_handling()

    print("\n=== 自动重试 ===")
    demo_retry()
