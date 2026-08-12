"""enumerate替代range(len())示例"""

# 错误写法
def bad_traverse():
    fruits = ["apple", "banana", "cherry"]
    for i in range(len(fruits)):
        print(f"  [bad]  {i}: {fruits[i]}")


# 推荐写法
def good_traverse():
    fruits = ["apple", "banana", "cherry"]
    for i, fruit in enumerate(fruits):
        print(f"  [good] {i}: {fruit}")


def enumerate_with_start():
    """指定起始索引"""
    fruits = ["apple", "banana", "cherry"]
    for i, fruit in enumerate(fruits, start=1):
        print(f"  第{i}个: {fruit}")


def enumerate_dict():
    """enumerate遍历字典项"""
    config = {"host": "localhost", "port": 8080, "debug": True}
    for i, (key, value) in enumerate(config.items()):
        print(f"  {i}: {key} = {value}")


def build_ranked_list():
    """实用场景：构建排名列表"""
    scores = [95, 87, 92, 78, 88]
    ranked = [(rank, name, score)
              for rank, (name, score) in
              enumerate(sorted(
                  [("Alice", 95), ("Bob", 87), ("Charlie", 92),
                   ("David", 78), ("Eve", 88)],
                  key=lambda x: -x[1]
              ), start=1)]
    for rank, name, score in ranked:
        print(f"  第{rank}名: {name} - {score}分")


if __name__ == "__main__":
    print("=== 错误写法 ===")
    bad_traverse()
    print("\n=== 推荐写法 ===")
    good_traverse()
    print("\n=== 指定起始索引 ===")
    enumerate_with_start()
    print("\n=== 遍历字典 ===")
    enumerate_dict()
    print("\n=== 排名列表 ===")
    build_ranked_list()
