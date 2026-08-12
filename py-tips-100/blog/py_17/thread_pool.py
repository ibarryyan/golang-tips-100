"""concurrent.futures 线程池演示"""
import concurrent.futures
import time


def simulate_io(task_id, duration=0.5):
    """模拟 I/O 操作"""
    time.sleep(duration)
    return f"task-{task_id} done"


def demo_map():
    """使用 map 批量执行"""
    task_ids = range(10)

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(simulate_io, task_ids))

    print(f"map 结果数: {len(results)}")
    print(f"前3个: {results[:3]}")


def demo_submit():
    """使用 submit + as_completed 逐个获取结果"""
    task_ids = range(10)

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        future_to_id = {
            executor.submit(simulate_io, tid): tid
            for tid in task_ids
        }
        for future in concurrent.futures.as_completed(future_to_id):
            tid = future_to_id[future]
            try:
                result = future.result()
                print(f"  {tid} -> {result}")
            except Exception as e:
                print(f"  {tid} -> error: {e}")


def demo_error_handling():
    """演示异常处理"""
    def risky_task(x):
        if x == 3:
            raise ValueError(f"bad value: {x}")
        return x * 2

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(risky_task, i) for i in range(5)]
        for future in concurrent.futures.as_completed(futures):
            try:
                print(f"  结果: {future.result()}")
            except ValueError as e:
                print(f"  异常: {e}")


if __name__ == "__main__":
    print("=== map 模式 ===")
    demo_map()

    print("\n=== submit + as_completed 模式 ===")
    demo_submit()

    print("\n=== 异常处理 ===")
    demo_error_handling()
