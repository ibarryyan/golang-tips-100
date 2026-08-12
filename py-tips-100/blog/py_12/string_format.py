"""字符串格式化的三种方式"""

name = "Tom"
age = 18

# 方式一：% 格式化（老旧写法，不推荐）
msg1 = "Name: %s, Age: %d" % (name, age)
print(msg1)

# 方式二：str.format()
msg2 = "Name: {}, Age: {}".format(name, age)
print(msg2)

msg2_named = "Name: {n}, Age: {a}".format(n=name, a=age)
print(msg2_named)

# 方式三：f-string（推荐）
msg3 = f"Name: {name}, Age: {age}"
print(msg3)

# 格式说明符
price = 3.14159
print(f"价格: ¥{price:.2f}")         # 保留两位小数
print(f"百分比: {0.875:.1%}")         # 百分比格式
print(f"二进制: {255:b}")             # 二进制
print(f"科学计数: {1234567:e}")       # 科学计数法

# 对齐
print(f"{'left':<10}|")    # 左对齐
print(f"{'center':^10}|")  # 居中
print(f"{'right':>10}|")   # 右对齐

# 填充字符
print(f"{42:08d}")  # 00000042

# f-string 支持表达式
items = [1, 2, 3]
print(f"总数: {len(items)}, 总和: {sum(items)}")

# 条件表达式
status = "pass"
print(f"结果: {'通过' if status == 'pass' else '失败'}")
