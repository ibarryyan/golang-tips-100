"""列表推导式vs生成器表达式"""

# === 列表推导式：一次性创建完整列表 ===
numbers = range(10)

# 列表推导式：立即计算，占用内存
squares_list = [x ** 2 for x in numbers]
print("列表推导式:", squares_list)
print("类型:", type(squares_list))  # <class 'list'>

# === 生成器表达式：惰性计算，节省内存 ===
squares_gen = (x ** 2 for x in numbers)
print("生成器表达式类型:", type(squares_gen))  # <class 'generator'>

# 需要时才逐个计算
print("逐个获取:", next(squares_gen), next(squares_gen))  # 0, 1

# 也可以转成列表
squares_gen2 = (x ** 2 for x in numbers)
print("转列表:", list(squares_gen2))

# === 内存对比 ===
import sys

big_list = [x ** 2 for x in range(10000)]
big_gen = (x ** 2 for x in range(10000))

print(f"列表占用: {sys.getsizeof(big_list)} bytes")
print(f"生成器占用: {sys.getsizeof(big_gen)} bytes")

# === 实际使用场景 ===

# 场景1：需要多次遍历 → 用列表推导式
data = [x * 2 for x in range(5)]
print("可多次遍历:", data, data)  # 列表可以反复访问

# 场景2：只需要遍历一次 → 用生成器表达式（尤其数据量大时）
# 例如求和：不需要先创建完整列表
total = sum(x ** 2 for x in range(1000))
print("生成器求和:", total)

# 场景3：配合 any/all 使用，提前终止
# 找到第一个偶数就停止
has_even = any(x % 2 == 0 for x in [1, 3, 5, 4, 7])
print("是否有偶数:", has_even)

# 场景4：大数据处理用生成器避免内存溢出
# 处理大文件行数
# lines = (line.strip() for line in open("big_file.txt"))  # 不会一次加载全部

# === 常见陷阱 ===

# 陷阱1：生成器只能遍历一次
gen = (x for x in range(5))
print("第一次:", list(gen))  # [0, 1, 2, 3, 4]
print("第二次:", list(gen))  # [] 已耗尽

# 陷阱2：在 lambda/闭包中引用推导式变量时的延迟绑定
# 见 closure_capture.py
