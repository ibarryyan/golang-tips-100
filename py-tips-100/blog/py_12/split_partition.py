"""split 和 partition 的用法"""

# split 按分隔符切割，返回列表
text = "Python,Java,Go,Rust"
langs = text.split(",")
print(f"split: {langs}")

# 限制分割次数
langs = text.split(",", maxsplit=2)
print(f"maxsplit=2: {langs}")

# partition 返回三元组
text = "user@example.com"
before, sep, after = text.partition("@")
print(f"partition: before={before}, sep={sep}, after={after}")

# 解析 key=value
config = "host=localhost"
key, _, value = config.partition("=")
print(f"key={key}, value={value}")

# rpartition 从右侧开始
path = "/usr/local/bin/python"
dir_name, _, base_name = path.rpartition("/")
print(f"目录: {dir_name}, 文件: {base_name}")

# rsplit 从右侧开始
text = "a.b.c.d.e"
parts = text.rsplit(".", maxsplit=2)
print(f"rsplit: {parts}")  # ['a.b.c', 'd', 'e']
