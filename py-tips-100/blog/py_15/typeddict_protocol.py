"""TypedDict 和 Protocol"""

from typing import TypedDict, Protocol


# === TypedDict: 给字典添加类型约束 ===

class UserDict(TypedDict):
    name: str
    age: int
    email: str

# 创建时 IDE 可以提示字段名和类型
user: UserDict = {"name": "Tom", "age": 18, "email": "tom@example.com"}

def send_email(user: UserDict) -> None:
    print(f"发送邮件到 {user['email']}")

send_email(user)

# total=False: 所有字段可选
class UpdateUser(TypedDict, total=False):
    name: str
    age: int
    email: str

# 所有字段都可以省略
update1: UpdateUser = {"age": 20}
update2: UpdateUser = {"name": "Jerry"}
update3: UpdateUser = {"name": "Spike", "email": "spike@example.com"}
print(f"更新1: {update1}")
print(f"更新2: {update2}")
print(f"更新3: {update3}")


# === Protocol: 结构化子类型（鸭子类型的类型安全版本） ===

class HasName(Protocol):
    name: str

class HasAge(Protocol):
    age: int

# 任何有 name 属性的对象都满足 HasName，无需继承
def greet(obj: HasName) -> str:
    return f"Hello, {obj.name}"

class User:
    def __init__(self, name: str):
        self.name = name

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

# User 和 Product 都满足 HasName 协议
print(greet(User("Tom")))
print(greet(Product("Widget")))

# 更复杂的 Protocol
class Drawable(Protocol):
    def draw(self) -> str: ...

def render(obj: Drawable) -> None:
    print(f"渲染: {obj.draw()}")

class Circle:
    def draw(self) -> str:
        return "圆形"

class Square:
    def draw(self) -> str:
        return "方形"

render(Circle())
render(Square())
