"""装饰器本质是函数包装函数"""

import time


# === 基础装饰器：计时 ===
def timer(func):
    """测量函数执行时间"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"[{func.__name__}] 耗时: {elapsed:.4f}s")
        return result
    return wrapper


@timer
def slow_function(n):
    """模拟耗时操作"""
    total = sum(i * i for i in range(n))
    return total


print("结果:", slow_function(100000))


# === 带参数的装饰器 ===
def repeat(times):
    """让函数重复执行 times 次"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


greet("World")  # 打印3次


# === 装饰器叠加：从下往上应用 ===
def uppercase_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


def exclaim_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!!!"
    return wrapper


@uppercase_result
@exclaim_result
def get_message():
    return "hello"


print("叠加装饰:", get_message())  # HELLO!!!


# === 类装饰器 ===
class CallCounter:
    """统计函数调用次数"""
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"[{self.func.__name__}] 第 {self.count} 次调用")
        return self.func(*args, **kwargs)


@CallCounter
def process(data):
    return f"processed-{data}"


print(process("a"))
print(process("b"))
print("总调用次数:", process.count)
