"""批量请求与限流控制示例"""
import time
from typing import Callable, TypeVar
from concurrent.futures import ThreadPoolExecutor, as_completed

T = TypeVar("T")
R = TypeVar("R")


class RateLimiter:
    """简单令牌桶限流器"""
    def __init__(self, max_calls: int, period: float = 1.0):
        self.max_calls = max_calls
        self.period = period
        self.calls: list[float] = []

    def acquire(self):
        now = time.time()
        self.calls = [t for t in self.calls if now - t < self.period]
        if len(self.calls) >= self.max_calls:
            sleep_time = self.period - (now - self.calls[0])
            if sleep_time > 0:
                time.sleep(sleep_time)
        self.calls.append(time.time())

    def stats(self) -> dict:
        now = time.time()
        recent = [t for t in self.calls if now - t < self.period]
        return {
            "recent_calls": len(recent),
            "max_calls": self.max_calls,
            "period": self.period,
        }


def batch_process(
    items: list[T],
    processor: Callable[[T], R],
    batch_size: int = 10,
    max_workers: int = 4,
    delay: float = 0.0
) -> list[R]:
    """批量并发处理，带限流"""
    results: list[R] = []
    total = len(items)

    for i in range(0, total, batch_size):
        batch = items[i:i + batch_size]
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(processor, item): item for item in batch}
            for future in as_completed(futures):
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    print(f"  [错误] 处理失败: {e}")
                    results.append(None)
        if delay > 0 and i + batch_size < total:
            time.sleep(delay)
        print(f"  进度: {min(i + batch_size, total)}/{total}")

    return results


def retry_on_failure(
    func: Callable,
    max_retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0
):
    """带指数退避的重试装饰器"""
    def wrapper(*args, **kwargs):
        last_error = None
        current_delay = delay
        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                last_error = e
                print(f"  [重试] 第{attempt + 1}/{max_retries}次失败: {e}")
                if attempt < max_retries - 1:
                    time.sleep(current_delay)
                    current_delay *= backoff
        raise last_error
    return wrapper


def mock_llm_call(prompt: str) -> str:
    """模拟LLM API调用"""
    return f"response: {prompt[:20]}..."


def demo_rate_limiter():
    """限流器演示"""
    print("=== 限流器 ===")
    limiter = RateLimiter(max_calls=5, period=1.0)

    for i in range(10):
        limiter.acquire()
        print(f"  第{i + 1}次调用 @ {time.strftime('%H:%M:%S')}")

    print(f"  限流器状态: {limiter.stats()}")


def demo_batch():
    """批量处理演示"""
    print("\n=== 批量处理 ===")
    prompts = [f"总结：文本内容第{i}段" for i in range(20)]
    results = batch_process(
        prompts,
        mock_llm_call,
        batch_size=5,
        max_workers=3,
        delay=0.5
    )
    success = sum(1 for r in results if r is not None)
    print(f"  成功: {success}/{len(prompts)}")


def demo_retry():
    """重试演示"""
    print("\n=== 重试机制 ===")
    call_count = 0

    @retry_on_failure(max_retries=3, delay=0.5, backoff=1.5)
    def flaky_api():
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            raise ConnectionError(f"连接失败 (第{call_count}次)")
        return "success"

    try:
        result = flaky_api()
        print(f"  最终结果: {result}")
        print(f"  总调用次数: {call_count}")
    except Exception as e:
        print(f"  彻底失败: {e}")


def demo_combined():
    """限流 + 重试 + 批量 组合"""
    print("\n=== 组合模式 ===")
    limiter = RateLimiter(max_calls=3, period=1.0)

    @retry_on_failure(max_retries=2, delay=0.3, backoff=2.0)
    def call_api(prompt: str) -> str:
        limiter.acquire()
        return f"result({prompt[:15]})"

    prompts = [f"prompt_{i}" for i in range(6)]
    results = batch_process(prompts, call_api, batch_size=3, max_workers=2, delay=0.5)
    for r in results:
        print(f"  {r}")


if __name__ == "__main__":
    demo_rate_limiter()
    demo_batch()
    demo_retry()
    demo_combined()
