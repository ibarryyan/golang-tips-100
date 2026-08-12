"""asyncio 超时和取消演示"""
import asyncio
import sys


async def slow_api():
    await asyncio.sleep(100)
    return "data"


async def demo_wait_for():
    """使用 wait_for 设置超时（所有版本通用）"""
    try:
        result = await asyncio.wait_for(slow_api(), timeout=1.0)
        print(result)
    except asyncio.TimeoutError:
        print("wait_for: 请求超时！")


async def demo_timeout_context():
    """使用 asyncio.timeout 上下文管理器（Python 3.11+）"""
    if sys.version_info < (3, 11):
        print("asyncio.timeout 需要 Python 3.11+，跳过")
        return
    try:
        async with asyncio.timeout(1.0):
            result = await slow_api()
            print(result)
    except asyncio.TimeoutError:
        print("asyncio.timeout: 请求超时！")


async def long_task():
    """可被取消的长时间任务"""
    try:
        await asyncio.sleep(10)
        print("任务完成了")  # 不会执行
    except asyncio.CancelledError:
        print("任务被取消")
        raise  # 建议重新抛出


async def demo_cancel():
    """取消任务"""
    task = asyncio.create_task(long_task())
    await asyncio.sleep(0.3)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("主协程收到取消信号")


async def demo_gather_cancel():
    """gather 中一个失败，取消其他"""
    async def task_ok(name, delay):
        await asyncio.sleep(delay)
        return f"{name}_ok"

    async def task_fail():
        await asyncio.sleep(0.2)
        raise ValueError("任务失败")

    tasks = [
        asyncio.create_task(task_ok("A", 1.0)),
        asyncio.create_task(task_fail()),
        asyncio.create_task(task_ok("B", 1.0)),
    ]
    try:
        await asyncio.gather(*tasks)
    except ValueError as e:
        print(f"gather 中异常: {e}")
    # 检查其他任务状态
    for i, t in enumerate(tasks):
        print(f"  task-{i} 状态: {'已取消' if t.cancelled() else '运行中' if not t.done() else '已完成'}")


async def main():
    print("=== wait_for 超时 ===")
    await demo_wait_for()

    print("\n=== asyncio.timeout 超时 ===")
    await demo_timeout_context()

    print("\n=== 取消任务 ===")
    await demo_cancel()

    print("\n=== gather 中的取消传播 ===")
    await demo_gather_cancel()


if __name__ == "__main__":
    asyncio.run(main())
