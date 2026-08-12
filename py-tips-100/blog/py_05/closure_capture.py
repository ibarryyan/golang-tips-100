"""闭包捕获的是变量引用而非值"""

functions = []

# 错误示例：在循环中创建闭包，捕获的是循环变量的引用
for i in range(3):
    functions.append(lambda: i)

# 所有函数返回的都是最后的值 2
print("错误示例:", [f() for f in functions])  # [2, 2, 2]

# 正确写法1：使用默认参数捕获当前值
functions_ok = []
for i in range(3):
    functions_ok.append(lambda x=i: x)

print("默认参数:", [f() for f in functions_ok])  # [0, 1, 2]

# 正确写法2：使用工厂函数
def make_func(x):
    return lambda: x

functions_factory = [make_func(i) for i in range(3)]
print("工厂函数:", [f() for f in functions_factory])  # [0, 1, 2]

# 正确写法3：列表推导式天然有独立作用域
functions_comp = [lambda x=x: x for x in range(3)]
print("推导式:", [f() for f in functions_comp])  # [0, 1, 2]

# 演示闭包捕获变量引用（可变）
counter = [0]


def make_counter():
    def increment():
        counter[0] += 1
        return counter[0]

    return increment


count = make_counter()
print("闭包引用:", count(), count(), count())  # 1, 2, 3
print("外部变量:", counter[0])  # 3
