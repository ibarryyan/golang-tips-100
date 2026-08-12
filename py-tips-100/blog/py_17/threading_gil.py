"""threading 模块基础与 GIL 限制演示"""
import threading
import time


def count_down(n):
    """CPU 密集型任务"""
    while n > 0:
        n -= 1


def io_task(url):
    """I/O 密集型任务"""
    import urllib.request
    return urllib.request.urlopen(url).read()


if __name__ == "__main__":
    # === CPU 密集型：多线程不会加速 ===
    N = 50_000_000

    start = time.time()
    t1 = threading.Thread(target=count_down, args=(N,))
    t2 = threading.Thread(target=count_down, args=(N,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"双线程(CPU密集): {time.time() - start:.2f}s")

    start = time.time()
    count_down(N)
    count_down(N)
    print(f"单线程(CPU密集): {time.time() - start:.2f}s")

    # === I/O 密集型：多线程显著加速 ===
    urls = ["https://httpbin.org/delay/1"] * 3

    start = time.time()
    threads = [threading.Thread(target=io_task, args=(url,)) for url in urls]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"多线程(I/O密集): {time.time() - start:.2f}s")

    start = time.time()
    for url in urls:
        io_task(url)
    print(f"单线程(I/O密集): {time.time() - start:.2f}s")
