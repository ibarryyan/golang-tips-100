"""__str__和__repr__的区别"""

import datetime


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __repr__：开发者友好，应能"重建对象"
    def __repr__(self):
        return f"User(name={self.name!r}, age={self.age})"

    # __str__：用户友好，可读性强
    def __str__(self):
        return f"用户 {self.name}，年龄 {self.age} 岁"


user = User("Alice", 30)

# print() 调用 __str__
print("print:", user)  # 用户 Alice，年龄 30 岁

# 直接在交互式环境或 repr() 调用 __repr__
print("repr:", repr(user))  # User(name='Alice', age=30)

# === 如果只实现一个，优先 __repr__ ===
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 只实现 __repr__，没实现 __str__
    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price})"


p = Product("Book", 29.9)
print("只实现repr:", p)  # print 会 fallback 到 __repr__
print("repr:", repr(p))

# === 列表/字典中的元素用 __repr__ ===
users = [User("Alice", 30), User("Bob", 25)]
print("列表中:", users)  # 用 __repr__ 显示每个元素

# === 标准库示例 ===
now = datetime.datetime(2025, 1, 15, 10, 30)
print("datetime str:", str(now))   # 2025-01-15 10:30:00
print("datetime repr:", repr(now))  # datetime.datetime(2025, 1, 15, 10, 30)

# === 实用建议 ===
# __repr__ 应包含足够信息来重建对象或调试
# __str__ 应面向最终用户，简洁可读
# 如果不确定，至少实现 __repr__，因为它会作为 __str__ 的 fallback
