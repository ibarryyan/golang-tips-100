"""dataclass 简化数据类定义"""

from dataclasses import dataclass, field
from typing import List


# 旧写法：手写所有方法
class UserOld:
    def __init__(self, name, age, email=""):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return f"UserOld(name={self.name!r}, age={self.age!r}, email={self.email!r})"

    def __eq__(self, other):
        return (self.name, self.age, self.email) == (other.name, other.age, other.email)


# 新写法：dataclass 自动生成
@dataclass
class User:
    name: str
    age: int
    email: str = ""
    tags: list = field(default_factory=list)  # 不能用 []，必须用 default_factory


u1 = User("Tom", 18)
u2 = User("Tom", 18)
print(f"自动 repr: {u1}")
print(f"自动 eq: {u1 == u2}")

# frozen=True 使实例不可变（可哈希）
@dataclass(frozen=True)
class Config:
    host: str
    port: int

cfg = Config("localhost", 8080)
print(f"配置: {cfg}")
# cfg.port = 9090  # FrozenInstanceError

# order=True 自动生成比较方法，支持排序
@dataclass(order=True)
class Score:
    value: int

scores = [Score(90), Score(85), Score(95)]
scores.sort()
print(f"排序后: {[s.value for s in scores]}")

# 嵌套 dataclass
@dataclass
class Team:
    name: str
    members: List[User] = field(default_factory=list)

team = Team("Backend", [u1, u2])
print(f"团队: {team.name}, 人数: {len(team.members)}")
