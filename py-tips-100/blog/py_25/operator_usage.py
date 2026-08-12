"""operator模块简化函数式写法示例"""
from operator import itemgetter, attrgetter, methodcaller
from functools import reduce
import operator


def demo_itemgetter():
    """itemgetter取字段"""
    print("=== itemgetter ===")
    students = [("Alice", 90), ("Bob", 85), ("Charlie", 95)]

    # 按分数排序
    by_score = sorted(students, key=itemgetter(1), reverse=True)
    print(f"  按分数排序: {by_score}")

    # 多字段排序
    data = [("A", 3, 2), ("A", 1, 5), ("A", 1, 3), ("B", 2, 1)]
    multi_sorted = sorted(data, key=itemgetter(0, 1, 2))
    print(f"  多字段排序: {multi_sorted}")

    # 取字典字段
    config = {"host": "localhost", "port": 8080, "debug": True}
    get_host_port = itemgetter("host", "port")
    print(f"  取字段: {get_host_port(config)}")


def demo_attrgetter():
    """attrgetter取属性"""
    print("\n=== attrgetter ===")
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def __repr__(self):
            return f"Point({self.x}, {self.y})"

    points = [Point(3, 4), Point(1, 2), Point(5, 0)]
    sorted_by_x = sorted(points, key=attrgetter("x"))
    print(f"  按x排序: {sorted_by_x}")

    sorted_by_y = sorted(points, key=attrgetter("y"))
    print(f"  按y排序: {sorted_by_y}")


def demo_methodcaller():
    """methodcaller调用方法"""
    print("\n=== methodcaller ===")
    words = ["Hello", "WORLD", "Python"]

    # 调用lower方法
    lower_words = list(map(methodcaller("lower"), words))
    print(f"  lower: {lower_words}")

    # 调用split方法
    urls = ["a/b/c", "d/e/f"]
    parts = list(map(methodcaller("split", "/"), urls))
    print(f"  split: {parts}")

    # 调用replace方法
    cleaned = list(map(methodcaller("replace", " ", "_"), ["hello world", "foo bar"]))
    print(f"  replace: {cleaned}")


def compare_lambda_vs_operator():
    """对比lambda和operator"""
    print("\n=== lambda vs operator ===")
    data = [("A", 3), ("B", 1), ("C", 2)]

    # lambda写法
    sorted_lambda = sorted(data, key=lambda x: x[1])
    print(f"  lambda: {sorted_lambda}")

    # operator写法（更简洁、更高效）
    sorted_op = sorted(data, key=itemgetter(1))
    print(f"  operator: {sorted_op}")


def reduce_with_operator():
    """reduce + operator"""
    print("\n=== reduce + operator ===")
    numbers = [1, 2, 3, 4, 5]

    # operator.add
    total = reduce(operator.add, numbers)
    print(f"  add: {total}")

    # operator.mul
    product = reduce(operator.mul, numbers)
    print(f"  mul: {product}")

    # operator.concat
    words = ["Hello", " ", "World"]
    combined = reduce(operator.concat, words)
    print(f"  concat: {combined}")

    # 对比：Python 3.8+ 的math.prod
    import math
    print(f"  math.prod: {math.prod(numbers)}")


def practical_usage():
    """实用场景"""
    print("\n=== 实用场景 ===")
    # 用itemgetter提取CSV行字段
    rows = [
        ("Alice", "25", "Engineer"),
        ("Bob", "30", "Designer"),
        ("Charlie", "28", "Manager"),
    ]
    get_name_role = itemgetter(0, 2)
    for row in rows:
        name, role = get_name_role(row)
        print(f"  {name}: {role}")


if __name__ == "__main__":
    demo_itemgetter()
    demo_attrgetter()
    demo_methodcaller()
    compare_lambda_vs_operator()
    reduce_with_operator()
    practical_usage()
