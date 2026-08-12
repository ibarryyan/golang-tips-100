"""namedtuple 给元组起名字"""

from collections import namedtuple
from typing import NamedTuple

# 普通元组 vs namedtuple
point_old = (10, 20)
print(f"普通元组: x={point_old[0]}, y={point_old[1]}")  # 索引访问，可读性差

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(f"namedtuple: x={p.x}, y={p.y}")
print(f"仍支持索引: x={p[0]}, y={p[1]}")

# 实际应用：模拟数据库返回行
User = namedtuple("User", ["name", "age", "email"])
rows = [
    ("Tom", 18, "tom@example.com"),
    ("Jerry", 25, "jerry@example.com"),
]
users = [User._make(row) for row in rows]
for u in users:
    print(f"  {u.name}, {u.age}, {u.email}")

# 使用 typing.NamedTuple 配合类型注解
class Point2D(NamedTuple):
    x: float
    y: float
    label: str = "default"

p2 = Point2D(1.0, 2.0)
print(f"带类型注解: {p2.x}, {p2.y}, label={p2.label}")

# namedtuple 是不可变的
try:
    p.x = 100  # AttributeError
except AttributeError as e:
    print(f"不可变: {e}")

# 用 _replace 创建修改后的副本
p3 = p._replace(x=100)
print(f"replace 后: {p3}, 原对象: {p}")
