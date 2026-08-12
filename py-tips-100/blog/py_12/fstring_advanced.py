"""f-string 高级用法：表达式、对齐、日期"""

from datetime import datetime

# 调试输出（Python 3.8+）
x = 42
y = "hello"
print(f"{x=}, {y=}")           # x=42, y='hello'
print(f"{x + 1=}")              # x + 1=43

# 日期格式化
now = datetime.now()
print(f"当前时间: {now:%Y-%m-%d %H:%M:%S}")
print(f"年月: {now:%Y年%m月}")
print(f"星期: {now:%A}")

# 多行 f-string
name = "Tom"
age = 18
city = "Beijing"
msg = (
    f"姓名: {name}\n"
    f"年龄: {age}\n"
    f"城市: {city}"
)
print(msg)

# 嵌套花括号控制宽度
width = 10
for i in range(1, 4):
    print(f"{i:{width}d}")

# 字典和对象访问
user = {"name": "Tom", "age": 18}
print(f"用户: {user['name']}")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(3, 4)
print(f"坐标: ({p.x}, {p.y})")
print(f"距离: {(p.x**2 + p.y**2)**0.5:.2f}")

# 注意：f-string 中不能使用反斜杠
name = "Tom\n"
# f"{name\n}"  # SyntaxError
print(f"{name}", end="")  # 正确写法
