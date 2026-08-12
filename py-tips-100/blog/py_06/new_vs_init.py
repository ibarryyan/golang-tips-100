"""__init__不是构造函数，__new__才是"""


# __new__ 创建实例，__init__ 初始化实例
class Person:
    def __new__(cls, *args, **kwargs):
        print(f"1. __new__ 被调用，创建实例")
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        print(f"2. __init__ 被调用，初始化实例")
        self.name = name


p = Person("Alice")
print("结果:", p.name)


# === 实际应用：单例模式 ===
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("创建新实例")
            cls._instance = super().__new__(cls)
        else:
            print("返回已有实例")
        return cls._instance

    def __init__(self, value):
        # 注意：__init__ 每次都会被调用
        if not hasattr(self, "value"):
            self.value = value


s1 = Singleton("first")
s2 = Singleton("second")
print("s1 is s2:", s1 is s2)  # True，同一个实例
print("value:", s1.value)  # first（只初始化了一次）


# === 实际应用：不可变类型 ===
# int、str、tuple 等不可变类型通过 __new__ 控制创建过程
class PositiveInt(int):
    def __new__(cls, value):
        if value < 0:
            raise ValueError("必须为正数")
        instance = super().__new__(cls, value)
        return instance


num = PositiveInt(42)
print("自定义int:", num, type(num))  # 42 PositiveInt

# 错误示例：__init__ 不能阻止对象创建
# class WrongPositiveInt(int):
#     def __init__(self, value):
#         if value < 0:
#             raise ValueError("必须为正数")  # 对象已经创建了！
