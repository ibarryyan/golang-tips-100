"""map/filter/reduce使用场景示例"""
from functools import reduce


def basic_map():
    """map基础用法"""
    numbers = [1, 2, 3, 4, 5]

    # map + lambda
    doubled = list(map(lambda x: x * 2, numbers))
    print(f"  map *2: {doubled}")

    # map + 命名函数（更推荐）
    upper_words = list(map(str.upper, ["hello", "world"]))
    print(f"  map upper: {upper_words}")

    # map多序列
    sums = list(map(lambda a, b: a + b, [1, 2, 3], [10, 20, 30]))
    print(f"  map多序列: {sums}")


def basic_filter():
    """filter基础用法"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # filter偶数
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"  filter偶数: {evens}")

    # filter去除None
    data = [1, None, 2, None, 3]
    clean = list(filter(None, data))  # None作为函数时过滤 falsy 值
    print(f"  filter None: {clean}")


def basic_reduce():
    """reduce基础用法"""
    numbers = [1, 2, 3, 4, 5]

    # 求和
    total = reduce(lambda a, b: a + b, numbers)
    print(f"  reduce求和: {total}")

    # 求积
    product = reduce(lambda a, b: a * b, numbers)
    print(f"  reduce求积: {product}")

    # 合并字典
    dicts = [{"a": 1}, {"b": 2}, {"c": 3}]
    merged = reduce(lambda a, b: {**a, **b}, dicts)
    print(f"  reduce合并字典: {merged}")


def compare_with_comprehension():
    """对比列表推导式"""
    numbers = range(10)

    # map/filter写法
    result1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
    print(f"  map/filter: {result1}")

    # 列表推导式（更Pythonic）
    result2 = [x ** 2 for x in numbers if x % 2 == 0]
    print(f"  列表推导式: {result2}")

    print(f"  结果相同: {result1 == result2}")


def practical_reduce():
    """reduce实用场景"""
    # 找最大值
    nums = [3, 1, 4, 1, 5, 9, 2, 6]
    max_val = reduce(lambda a, b: a if a > b else b, nums)
    print(f"  reduce找最大: {max_val}")

    # 嵌套列表扁平化
    nested = [[1, 2], [3, 4], [5, 6]]
    flat = reduce(lambda a, b: a + b, nested)
    print(f"  reduce扁平化: {flat}")

    # 构建计数字典
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    count = reduce(
        lambda acc, w: {**acc, w: acc.get(w, 0) + 1},
        words,
        {}
    )
    print(f"  reduce计数: {count}")


if __name__ == "__main__":
    print("=== map ===")
    basic_map()
    print("\n=== filter ===")
    basic_filter()
    print("\n=== reduce ===")
    basic_reduce()
    print("\n=== 对比列表推导式 ===")
    compare_with_comprehension()
    print("\n=== reduce实用场景 ===")
    practical_reduce()
