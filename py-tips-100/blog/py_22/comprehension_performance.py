"""列表推导式 vs map/filter 性能对比演示"""
import timeit
import sys


data = list(range(100000))


# === 不同方式创建列表 ===
def list_comprehension():
    return [x * 2 for x in data]


def map_lambda():
    return list(map(lambda x: x * 2, data))


def for_loop():
    result = []
    for x in data:
        result.append(x * 2)
    return result


def gen_expression():
    return list(x * 2 for x in data)


# === 带过滤 ===
def comp_filter():
    return [x for x in data if x % 2 == 0]


def filter_lambda():
    return list(filter(lambda x: x % 2 == 0, data))


# === 内存对比 ===
def demo_memory():
    """列表 vs 生成器内存占用"""
    # 列表推导式：一次性创建
    lst = [x * 2 for x in range(1000000)]
    print(f"列表推导式: {sys.getsizeof(lst)} 字节 ({len(lst)} 个元素)")

    # 生成器表达式：惰性求值
    gen = (x * 2 for x in range(1000000))
    print(f"生成器表达式: {sys.getsizeof(gen)} 字节 (几乎不占内存)")


def benchmark():
    """性能基准测试"""
    funcs = [
        ("列表推导式", list_comprehension),
        ("map+lambda", map_lambda),
        ("for循环", for_loop),
        ("生成器表达式", gen_expression),
    ]

    print("=== 创建列表性能对比 ===")
    for name, func in funcs:
        t = timeit.timeit(func, number=1000)
        print(f"  {name}: {t / 1000:.6f}s/次")

    print("\n=== 过滤性能对比 ===")
    for name, func in [("列表推导式", comp_filter), ("filter+lambda", filter_lambda)]:
        t = timeit.timeit(func, number=1000)
        print(f"  {name}: {t / 1000:.6f}s/次")


if __name__ == "__main__":
    benchmark()

    print("\n=== 内存对比 ===")
    demo_memory()

    print("\n选择建议:")
    print("  小数据 + 需索引访问  → 列表推导式")
    print("  大数据 + 只遍历一次  → 生成器表达式")
    print("  已有函数（非lambda） → map/filter")
    print("  复杂逻辑 + break     → for 循环")
