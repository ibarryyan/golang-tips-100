"""zip并行遍历多个序列示例"""
from itertools import zip_longest


def basic_zip():
    """基础zip用法"""
    names = ["Alice", "Bob", "Charlie"]
    scores = [90, 85, 95]

    for name, score in zip(names, scores):
        print(f"  {name}: {score}")


def zip_three():
    """三个序列并行"""
    ids = [1, 2, 3]
    names = ["Alice", "Bob", "Charlie"]
    scores = [90, 85, 95]

    for id_, name, score in zip(ids, names, scores):
        print(f"  [{id_}] {name}: {score}")


def zip_longest_demo():
    """zip_longest处理不等长序列"""
    short = [1, 2]
    long = [1, 2, 3, 4]

    print("zip（以最短为准）:")
    for s, l in zip(short, long):
        print(f"  {s}, {l}")

    print("zip_longest（以最长为准）:")
    for s, l in zip_longest(short, long, fillvalue=0):
        print(f"  {s}, {l}")


def unzip_demo():
    """用zip解压"""
    pairs = [("Alice", 90), ("Bob", 85), ("Charlie", 95)]
    names, scores = zip(*pairs)

    print(f"  names: {names}")
    print(f"  scores: {scores}")


def zip_dict():
    """用zip构建字典"""
    keys = ["name", "age", "city"]
    values = ["Tom", 25, "Beijing"]
    data = dict(zip(keys, values))
    print(f"  {data}")


def zip_matrix():
    """zip实现矩阵转置"""
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    transposed = [list(row) for row in zip(*matrix)]
    print("  原矩阵:")
    for row in matrix:
        print(f"    {row}")
    print("  转置后:")
    for row in transposed:
        print(f"    {row}")


if __name__ == "__main__":
    print("=== 基础zip ===")
    basic_zip()
    print("\n=== 三序列并行 ===")
    zip_three()
    print("\n=== zip_longest ===")
    zip_longest_demo()
    print("\n=== 解压 ===")
    unzip_demo()
    print("\n=== 构建字典 ===")
    zip_dict()
    print("\n=== 矩阵转置 ===")
    zip_matrix()
