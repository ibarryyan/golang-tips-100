"""生成器函数用yield暂停执行"""


def count_up_to(n):
    """简单的生成器：从 1 计数到 n"""
    current = 1
    while current <= n:
        yield current
        current += 1


# 使用
for num in count_up_to(5):
    print(num, end=" ")  # 1 2 3 4 5
print()

# 手动调用
gen = count_up_to(3)
print("next:", next(gen))  # 1
print("next:", next(gen))  # 2
print("next:", next(gen))  # 3
# print(next(gen))  # StopIteration


# === yield 的暂停特性 ===
def echo_generator():
    """yield 可以接收外部通过 send() 传入的值"""
    print("生成器启动")
    while True:
        received = yield  # 接收 send 的值
        if received is None:
            break
        print(f"收到: {received}")


gen = echo_generator()
next(gen)        # 启动生成器，执行到第一个 yield
gen.send("hello")  # 输出: 收到: hello
gen.send("world")  # 输出: 收到: world
gen.close()      # 关闭生成器


# === 实用场景1：读取大文件 ===
def read_lines(filepath, batch_size=1000):
    """分批读取文件行，避免一次性加载"""
    with open(filepath, "r", encoding="utf-8") as f:
        batch = []
        for line in f:
            batch.append(line.strip())
            if len(batch) >= batch_size:
                yield batch
                batch = []
        if batch:
            yield batch


# === 实用场景2：无限序列 ===
def fibonacci():
    """斐波那契数列生成器"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
first_10 = [next(fib) for _ in range(10)]
print("斐波那契前10:", first_10)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# === yield from：委托给子生成器 ===
def chain_generators(*iterables):
    """将多个可迭代对象串联"""
    for iterable in iterables:
        yield from iterable


result = list(chain_generators([1, 2], [3, 4], [5, 6]))
print("yield from:", result)  # [1, 2, 3, 4, 5, 6]


# === 生成器 vs 列表 ===
# 生成器：惰性计算，不占内存
# 列表：立即计算，占用内存
# 大数据场景优先用生成器
