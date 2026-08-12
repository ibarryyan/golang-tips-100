"""List/Dict/Tuple 泛型注解"""

import sys

if sys.version_info >= (3, 9):
    # Python 3.9+ 直接使用内置类型
    def average(scores: list[float]) -> float:
        return sum(scores) / len(scores)

    def count_words(text: str) -> dict[str, int]:
        from collections import Counter
        return dict(Counter(text.split()))

    def get_point() -> tuple[float, float]:
        return 1.0, 2.0

    def unique_tags(tags: set[str]) -> set[str]:
        return tags

    # 变长元组
    def process_items(items: tuple[str, ...]) -> int:
        return len(items)
else:
    from typing import List, Dict, Tuple, Set
    # Python 3.8 使用 typing 模块
    def average(scores: List[float]) -> float:
        return sum(scores) / len(scores)

    def count_words(text: str) -> Dict[str, int]:
        from collections import Counter
        return dict(Counter(text.split()))

    def get_point() -> Tuple[float, float]:
        return 1.0, 2.0

    def unique_tags(tags: Set[str]) -> Set[str]:
        return tags

# 测试
print(average([90, 85, 95, 88]))
print(count_words("hello world hello python"))
print(get_point())
print(unique_tags({"python", "go", "rust"}))

# 嵌套类型注解
from typing import List, Dict, Union
if sys.version_info >= (3, 9):
    users: list[dict[str, "int | str"]] = [
        {"name": "Tom", "age": 18},
        {"name": "Jerry", "age": 25},
    ]
else:
    users: List[Dict[str, Union[int, str]]] = [
        {"name": "Tom", "age": 18},
        {"name": "Jerry", "age": 25},
    ]

for u in users:
    print(f"  {u['name']}, {u['age']}")

# 字符串到列表的映射
word_index: dict[str, list[int]] = {
    "apple": [0, 2, 5],
    "banana": [1, 3],
}
for word, indices in word_index.items():
    print(f"  {word}: {indices}")
