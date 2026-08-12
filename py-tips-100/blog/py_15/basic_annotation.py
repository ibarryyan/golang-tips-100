"""基本类型注解语法"""

# 变量注解
name: str = "Tom"
age: int = 18
score: float = 95.5
is_active: bool = True

# 函数注解
def greet(name: str, times: int = 1) -> str:
    return f"Hello, {name}! " * times

# 返回 None
def print_info(name: str, age: int) -> None:
    print(f"{name}, {age}")

# 调用
print(greet("Tom"))
print(greet("Jerry", times=3))
print_info("Spike", 30)

# 类型注解只是提示，运行时不强制检查
def add(a: int, b: int) -> int:
    return a + b

# 运行时不报错，但 mypy/pyright 会标记
result = add("1", 2)  # 返回 "12"
print(f"add('1', 2) = {result}")

# 使用 typing 模块的特殊类型
from typing import Any, NoReturn

def log_message(msg: Any) -> None:
    print(f"[LOG] {msg}")

def fatal_error() -> NoReturn:
    raise RuntimeError("致命错误")

log_message("测试消息")
log_message(123)
log_message([1, 2, 3])
