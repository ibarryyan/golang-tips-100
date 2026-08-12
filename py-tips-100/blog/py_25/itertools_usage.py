"""itertools常用工具函数示例"""
from itertools import (
    chain, combinations, permutations, product,
    groupby, islice, count, cycle, repeat, accumulate, starmap
)


def demo_chain():
    """chain拼接序列"""
    print("=== chain ===")
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined = list(chain(list1, list2))
    print(f"  chain: {combined}")

    # chain.from_iterable扁平化
    nested = [[1, 2], [3, 4], [5, 6]]
    flat = list(chain.from_iterable(nested))
    print(f"  from_iterable: {flat}")


def demo_islice():
    """islice切片惰性序列"""
    print("\n=== islice ===")
    first_5 = list(islice(range(100), 5))
    print(f"  前5个: {first_5}")

    middle = list(islice(range(20), 5, 10))
    print(f"  5-10: {middle}")

    with_step = list(islice(range(20), 0, 20, 3))
    print(f"  步长3: {with_step}")


def demo_groupby():
    """groupby分组"""
    print("\n=== groupby ===")
    data = [("A", 1), ("A", 2), ("B", 3), ("B", 4), ("C", 5)]
    for key, group in groupby(data, key=lambda x: x[0]):
        print(f"  {key}: {list(group)}")

    # 按数值范围分组
    numbers = [1, 2, 3, 5, 6, 8, 9, 10]
    for threshold, group in groupby(numbers, key=lambda x: (x - 1) // 3):
        print(f"  区间{threshold}: {list(group)}")


def demo_combinations():
    """combinations和permutations"""
    print("\n=== combinations/permutations ===")
    # 组合C(4,2)
    for combo in combinations("ABCD", 2):
        print(f"  组合: {combo}")

    # 排列P(3,2)
    for perm in permutations("ABC", 2):
        print(f"  排列: {perm}")


def demo_product():
    """product笛卡尔积"""
    print("\n=== product ===")
    for combo in product("AB", "12"):
        print(f"  {combo}")

    # repeat参数
    for combo in product("01", repeat=3):
        print(f"  3位二进制: {combo}")


def demo_infinite():
    """count/cycle/repeat无限迭代器"""
    print("\n=== 无限迭代器 ===")
    # count：无限计数
    for i in islice(count(10, 2), 5):
        print(f"  count: {i}")

    # cycle：循环
    for item in islice(cycle("AB"), 5):
        print(f"  cycle: {item}")

    # repeat：重复
    for item in islice(repeat("hello", 3), 5):
        print(f"  repeat: {item}")


def demo_accumulate():
    """accumulate累积"""
    print("\n=== accumulate ===")
    nums = [1, 2, 3, 4, 5]
    cumulative = list(accumulate(nums))
    print(f"  累积和: {cumulative}")

    import operator
    cumulative_mul = list(accumulate(nums, operator.mul))
    print(f"  累积积: {cumulative_mul}")


def large_file_demo():
    """模拟大文件处理"""
    print("\n=== 大文件前N行 ===")
    lines = [f"line_{i}" for i in range(1000)]
    for line in islice(lines, 5):
        print(f"  {line}")


if __name__ == "__main__":
    demo_chain()
    demo_islice()
    demo_groupby()
    demo_combinations()
    demo_product()
    demo_infinite()
    demo_accumulate()
    large_file_demo()
