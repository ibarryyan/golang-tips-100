"""class属性与实例属性的区别"""


class Dog:
    # 类属性：所有实例共享
    species = "Canis lupus"
    legs = 4

    def __init__(self, name):
        # 实例属性：每个实例独有
        self.name = name

    def describe(self):
        return f"{self.name} has {self.legs} legs, species: {self.species}"


# 创建实例
dog1 = Dog("Buddy")
dog2 = Dog("Max")

# 访问类属性（所有实例共享）
print("类属性:", dog1.species, dog2.species)  # Canis lupus Canis lupus

# 访问实例属性（各自独立）
print("实例属性:", dog1.name, dog2.name)  # Buddy Max

# === 陷阱1：通过实例修改类属性 → 变成了实例属性 ===
dog1.legs = 3  # 只修改了 dog1 的 legs，不影响 Dog 类
print("dog1.legs:", dog1.legs)   # 3
print("dog2.legs:", dog2.legs)   # 4
print("Dog.legs:", Dog.legs)     # 4

# === 陷阱2：可变类属性被所有实例共享 ===
class Config:
    # 危险：可变对象作为类属性
    settings = {}  # 所有实例共享同一个 dict！

    def __init__(self, env):
        self.settings["env"] = env  # 修改的是类的 settings

c1 = Config("dev")
c2 = Config("prod")
print("c1.settings:", c1.settings)  # {'env': 'prod'} ← 被覆盖了！
print("c2.settings:", c2.settings)  # {'env': 'prod'}

# 正确做法：在 __init__ 中初始化可变属性
class ConfigFixed:
    def __init__(self, env):
        self.settings = {"env": env}  # 每个实例独立的 dict

c1 = ConfigFixed("dev")
c2 = ConfigFixed("prod")
print("修正后 c1:", c1.settings)  # {'env': 'dev'}
print("修正后 c2:", c2.settings)  # {'env': 'prod'}
