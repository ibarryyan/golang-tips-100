"""set 去重原理和注意事项"""

# 基本去重
nums = [1, 2, 2, 3, 3, 3]
unique = list(set(nums))
print(f"set 去重: {unique}")  # 顺序不保证

# 保持原始顺序的去重
nums_ordered = [3, 1, 2, 2, 3]
unique_ordered = list(dict.fromkeys(nums_ordered))
print(f"保持顺序去重: {unique_ordered}")  # [3, 1, 2]

# 集合运算
a = {1, 2, 3}
b = {2, 3, 4}
print(f"交集: {a & b}")    # {2, 3}
print(f"并集: {a | b}")    # {1, 2, 3, 4}
print(f"差集: {a - b}")    # {1}
print(f"对称差集: {a ^ b}")  # {1, 4}

# 不可哈希类型不能放入 set
try:
    s = set()
    s.add([1, 2])  # TypeError
except TypeError as e:
    print(f"错误: {e}")

# 用元组代替列表
s = set()
s.add((1, 2))
s.add((3, 4))
print(f"元组集合: {s}")
