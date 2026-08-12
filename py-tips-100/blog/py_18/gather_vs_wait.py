"""asyncio.gather 和 wait 的区别演示"""
import asyncio


async def fetch(name, delay):
    await asyncio.sleep(delay)
    return f"{name}"


async def demo_gather():
    """gather：按传入顺序返回结果列表"""
    results = await asyncio.gather(
        fetch("A", 0.3),
        fetch("B", 0.1),
        fetch("C", 0.2),
    )
    print(f"gather 结果: {results}")  # ['A', 'B', 'C']


async def demo_gather_exceptions():
    """gather 异常处理"""
    async def risky(name, delay):
        await asyncio.sleep(delay)
        if name == "B":
            raise ValueError(f"{name} 出错")
        return name

    # return_exceptions=True：异常作为结果返回
    results = await asyncio.gather(
        risky("A", 0.1),
        risky("B", 0.2),
        risky("C", 0.3),
        return_exceptions=True,
    )
    for r in results:
        if isinstance(r, Exception):
            print(f"  异常: {r}")
        else:
            print(f"  正常: {r}")


async def demo_wait():
    """wait：返回 done 和 pending 集合"""
    tasks = [
        asyncio.create_task(fetch("A", 0.3)),
        asyncio.create_task(fetch("B", 0.1)),
        asyncio.create_task(fetch("C", 0.2)),
    ]
    done, pending = await asyncio.wait(tasks)
    print(f"wait 完成: {len(done)}, 未完成: {len(pending)}")
    for task in done:
        print(f"  {task.result()}")


async def demo_wait_first():
    """wait + FIRST_COMPLETED：第一个完成就返回"""
    tasks = [
        asyncio.create_task(fetch("A", 0.3)),
        asyncio.create_task(fetch("B", 0.1)),
        asyncio.create_task(fetch("C", 0.2)),
    ]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for task in done:
        print(f"  第一个完成: {task.result()}")
    for task in pending:
        task.cancel()


async def main():
    print("=== gather ===")
    await demo_gather()

    print("\n=== gather 异常处理 ===")
    await demo_gather_exceptions()

    print("\n=== wait ===")
    await demo_wait()

    print("\n=== wait FIRST_COMPLETED ===")
    await demo_wait_first()


if __name__ == "__main__":
    asyncio.run(main())
