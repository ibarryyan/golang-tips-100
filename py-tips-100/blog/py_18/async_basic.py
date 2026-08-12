"""async/await 基础语法演示"""
import asyncio


async def hello():
    print("hello async")
    await asyncio.sleep(0.5)  # 模拟异步操作
    print("hello done")


async def fetch_data(name, delay):
    """模拟异步获取数据"""
    print(f"  开始获取 {name}")
    await asyncio.sleep(delay)
    print(f"  {name} 获取完成")
    return f"{name}_data"


async def main():
    # 单个协程
    await hello()

    # 串行执行（不推荐）
    import time
    start = time.time()
    r1 = await fetch_data("A", 0.3)
    r2 = await fetch_data("B", 0.3)
    print(f"串行结果: {r1}, {r2}, 耗时: {time.time() - start:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
