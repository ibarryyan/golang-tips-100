"""事件循环和 Task 演示"""
import asyncio
import time


async def fetch_data(name, delay):
    print(f"  开始 {name}")
    await asyncio.sleep(delay)
    print(f"  完成 {name}")
    return f"{name}_data"


async def serial_demo():
    """串行 await：总耗时 = 各任务耗时之和"""
    start = time.time()
    r1 = await fetch_data("A", 0.3)
    r2 = await fetch_data("B", 0.3)
    r3 = await fetch_data("C", 0.3)
    print(f"串行: {r1}, {r2}, {r3} | 耗时: {time.time() - start:.2f}s")


async def concurrent_demo():
    """create_task 并发执行：总耗时 ≈ 最慢的任务"""
    start = time.time()
    task1 = asyncio.create_task(fetch_data("A", 0.3))
    task2 = asyncio.create_task(fetch_data("B", 0.3))
    task3 = asyncio.create_task(fetch_data("C", 0.3))

    r1 = await task1
    r2 = await task2
    r3 = await task3
    print(f"并发: {r1}, {r2}, {r3} | 耗时: {time.time() - start:.2f}s")


async def main():
    print("=== 串行执行 ===")
    await serial_demo()

    print("\n=== 并发执行 ===")
    await concurrent_demo()


if __name__ == "__main__":
    asyncio.run(main())
