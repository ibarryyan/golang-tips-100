"""multiprocessing 模块基础演示"""
import multiprocessing
import time


def compute(n):
    """CPU 密集型计算"""
    total = 0
    for i in range(n):
        total += i * i
    return total


def demo_pool():
    """使用进程池并行计算"""
    N = 5_000_000

    start = time.time()
    with multiprocessing.Pool(2) as pool:
        results = pool.map(compute, [N, N])
    print(f"双进程: {time.time() - start:.2f}s, 结果: {results}")

    start = time.time()
    r1 = compute(N)
    r2 = compute(N)
    print(f"单进程: {time.time() - start:.2f}s, 结果: [{r1}, {r2}]")


def demo_queue():
    """进程间通信：使用 Queue"""
    def producer(q):
        for i in range(5):
            q.put(f"item-{i}")
        q.put(None)  # 结束信号

    def consumer(q):
        while True:
            item = q.get()
            if item is None:
                break
            print(f"  消费: {item}")

    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=producer, args=(q,))
    p2 = multiprocessing.Process(target=consumer, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == "__main__":
    print("=== 进程池并行 ===")
    demo_pool()

    print("\n=== 进程间通信 ===")
    demo_queue()
