"""functools.wraps保留被装饰函数的元信息"""

import functools
import time


# === 不使用 wraps 的问题 ===
def timer_no_wrap(func):
    """不使用 functools.wraps 的装饰器"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"耗时: {time.time() - start:.4f}s")
        return result
    return wrapper


@timer_no_wrap
def my_function(x, y):
    """这是 my_function 的文档字符串"""
    return x + y


# 问题：装饰后，函数的元信息丢失了
print("函数名:", my_function.__name__)  # wrapper（不是 my_function！）
print("文档:", my_function.__doc__)    # None（文档字符串丢了！）


# === 正确做法：使用 functools.wraps ===
def timer(func):
    """使用 functools.wraps 保留元信息"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"耗时: {time.time() - start:.4f}s")
        return result
    return wrapper


@timer
def my_function_fixed(x, y):
    """这是 my_function_fixed 的文档字符串"""
    return x + y


print("修正后函数名:", my_function_fixed.__name__)  # my_function_fixed
print("修正后文档:", my_function_fixed.__doc__)     # 这是 my_function_fixed 的文档字符串


# === wraps 还保留了什么 ===
print("\n保留的属性:")
print("  __name__:", my_function_fixed.__name__)
print("  __doc__:", my_function_fixed.__doc__)
print("  __wrapped__:", my_function_fixed.__wrapped__)  # 原始函数

# 可以通过 __wrapped__ 直接访问原始函数
print("  原始函数调用:", my_function_fixed.__wrapped__(3, 4))  # 7


# === 带参数装饰器也必须用 wraps ===
def retry(max_attempts=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"第 {attempt + 1} 次失败: {e}")
            raise last_exception
        return wrapper
    return decorator


@retry(max_attempts=3)
def unstable_api():
    """不稳定API调用"""
    import random
    if random.random() < 0.7:
        raise ConnectionError("连接失败")
    return "success"


print("\n元信息:", unstable_api.__name__, unstable_api.__doc__)
