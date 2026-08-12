"""Counter 统计元素频次"""

from collections import Counter

# 基本计数
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counter = Counter(words)
print(f"计数结果: {counter}")

# 最常见元素
print(f"Top 2: {counter.most_common(2)}")

# 访问计数（不存在的返回 0）
print(f"apple 出现 {counter['apple']} 次")
print(f"missing 出现 {counter['missing']} 次")

# 更新计数
counter.update(["banana", "cherry", "cherry"])
print(f"更新后: {counter}")

# 计数器加减
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(f"相加: {c1 + c2}")
print(f"相减: {c1 - c2}")

# 统计字符串中字符频次
text = "hello world"
char_counter = Counter(text)
print(f"字符频次 Top 3: {char_counter.most_common(3)}")
