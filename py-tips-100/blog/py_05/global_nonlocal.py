"""global和nonlocal的使用场景"""

# === global：在函数内修改模块级变量 ===

count = 0


def increment_wrong():
    # 这样只是创建了一个局部变量，不会影响外部的 count
    count = 1
    return count


def increment_right():
    # 使用 global 声明后，赋值会影响模块级变量
    global count
    count += 1
    return count


increment_wrong()
print("错误修改后 count:", count)  # 0（没变）

increment_right()
print("global修改后 count:", count)  # 1


# === nonlocal：在嵌套函数中修改外层函数的变量 ===

def make_counter():
    """闭包计数器：用 nonlocal 修改外层变量"""
    total = 0

    def increment():
        nonlocal total
        total += 1
        return total

    def decrement():
        nonlocal total
        total -= 1
        return total

    return increment, decrement


inc, dec = make_counter()
print("计数器:", inc(), inc(), inc())  # 1, 2, 3
print("回退:", dec())  # 2


# === 不使用 global/nonlocal 的替代方案 ===

# 方案1：用可变对象绕过（不推荐，但可行）
def make_counter_v2():
    total = [0]

    def increment():
        total[0] += 1
        return total[0]

    return increment


counter2 = make_counter_v2()
print("可变对象:", counter2(), counter2())  # 1, 2

# 方案2：用类替代（推荐）
class Counter:
    def __init__(self):
        self._count = 0

    def increment(self):
        self._count += 1
        return self._count


c = Counter()
print("类计数器:", c.increment(), c.increment())  # 1, 2

# 总结：
# global 用于函数内修改模块级变量
# nonlocal 用于嵌套函数修改外层函数的变量
# 如果逻辑复杂，优先用类来组织状态
