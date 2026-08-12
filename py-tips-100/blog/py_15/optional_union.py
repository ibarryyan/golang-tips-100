"""Optional 和 Union 的使用"""

from typing import Optional, Union

# Optional 表示值可以为 None
def get_user_name(user_id: int) -> Optional[str]:
    if user_id <= 0:
        return None
    return "Tom"

result = get_user_name(1)
if result is not None:
    print(f"用户名: {result}")

result = get_user_name(-1)
print(f"无效用户: {result}")

# Union 表示多种类型
def process(data: Union[str, bytes]) -> str:
    if isinstance(data, bytes):
        return data.decode("utf-8")
    return data

print(process("hello"))
print(process(b"world"))

# Union 多个类型
def parse_value(value: Union[int, float, str]) -> float:
    return float(value)

print(parse_value(42))
print(parse_value(3.14))
print(parse_value("100"))

# Python 3.10+ 语法糖（如果在 3.10+ 环境运行）
import sys
if sys.version_info >= (3, 10):
    # | 语法
    def get_name(user_id: int) -> str | None:
        if user_id <= 0:
            return None
        return "Tom"

    def process_data(data: str | bytes) -> str:
        if isinstance(data, bytes):
            return data.decode("utf-8")
        return data

    # isinstance 也支持 |
    x = 42
    if isinstance(x, int | float):
        print(f"x 是数字: {x}")
