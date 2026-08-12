"""Lock 和 RLock 演示"""
import threading


# === 不加锁导致数据竞争 ===
def unsafe_increment():
    counter = 0

    def increment():
        nonlocal counter
        for _ in range(100000):
            counter += 1

    t1 = threading.Thread(target=increment)
    t2 = threading.Thread(target=increment)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"不加锁: {counter} (期望 200000)")


# === 使用 Lock 保护共享资源 ===
def safe_increment():
    counter = 0
    lock = threading.Lock()

    def increment():
        nonlocal counter
        for _ in range(100000):
            with lock:
                counter += 1

    t1 = threading.Thread(target=increment)
    t2 = threading.Thread(target=increment)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"加Lock: {counter} (期望 200000)")


# === RLock 可重入锁，适合递归 ===
def rlock_demo():
    rlock = threading.RLock()
    call_stack = []

    def recursive_func(n):
        with rlock:
            call_stack.append(n)
            if n > 0:
                recursive_func(n - 1)

    recursive_func(5)
    print(f"RLock递归调用栈: {call_stack}")


if __name__ == "__main__":
    unsafe_increment()
    safe_increment()
    rlock_demo()
