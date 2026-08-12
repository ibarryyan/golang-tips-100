"""lambda是匿名函数但能力有限"""

# lambda 基本用法：简单的一行表达式
add = lambda a, b: a + b
print("lambda 加法:", add(3, 5))  # 8

# 常见场景：作为排序的 key
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]

# 用 lambda 指定排序依据
sorted_people = sorted(people, key=lambda p: p["age"])
print("按年龄排序:", [p["name"] for p in sorted_people])

# 但 lambda 不能包含语句（如 if-else 块、for、while、赋值）
# 下面这种复杂逻辑不适合用 lambda：
# filter_data = lambda data: [x for x in data if x > 0 if x < 100]  # 可读性差

# 推荐用普通函数处理复杂逻辑
def filter_data(data):
    """过滤有效数据，复杂逻辑用普通函数更清晰"""
    result = []
    for x in data:
        if x > 0 and x < 100:
            result.append(x)
    return result


print("普通函数过滤:", filter_data([-5, 10, 50, 200, 30]))

# lambda 的限制：不能有语句，只能有表达式
# 错误示例（会报语法错误）：
# bad = lambda x: (x = 1; return x)  # SyntaxError

# lambda 不能直接使用赋值表达式（Python 3.8+ 可用海象运算符绕过）
# 但不推荐，可读性极差
numbers = [1, 2, 3, 4, 5]
# 带条件的 lambda
result = list(map(lambda x: x * 2 if x % 2 == 0 else x, numbers))
print("条件lambda:", result)  # [1, 4, 3, 8, 5]

# 总结：lambda 适合简单的内联操作，复杂逻辑请用 def
