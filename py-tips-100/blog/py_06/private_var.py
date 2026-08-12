"""私有变量靠约定不靠强制"""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner          # 公开属性
        self._balance = balance     # 约定私有（单下划线）
        self.__id = hash(owner)    # 名称重整（双下划线）

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        return self._balance

    def get_balance(self):
        return self._balance

    def get_id(self):
        return self.__id


acc = BankAccount("Alice", 1000)

# 公开属性：随意访问
print("owner:", acc.owner)  # Alice

# 单下划线：可以访问但不建议（约定私有）
print("_balance:", acc._balance)  # 1000（能访问，但你不应该这样做）

# 双下划线：名称重整后不能直接访问
# print(acc.__id)  # AttributeError!
# 但可以通过重整后的名字访问
print("重整名称:", acc._BankAccount__id)  # 可以但强烈不建议

# 推荐做法：通过方法访问
print("get_balance:", acc.get_balance())

# === property：用方法控制访问 ===
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius  # 内部用 _ 存储

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32


temp = Temperature(25)
print("摄氏度:", temp.celsius)       # 25（像属性一样访问）
print("华氏度:", temp.fahrenheit)    # 77.0

temp.celsius = 30
print("修改后:", temp.celsius)       # 30

# temp.celsius = -300  # ValueError!
