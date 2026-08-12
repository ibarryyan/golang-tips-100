"""正则表达式 re 模块基础"""

import re

# 查找第一个匹配
text = "My phone is 138-0013-8000"
match = re.search(r"\d{3}-\d{4}-\d{4}", text)
if match:
    print(f"找到电话: {match.group()}")

# 全部匹配
text = "2024-01-15 and 2024-06-20"
dates = re.findall(r"\d{4}-\d{2}-\d{2}", text)
print(f"日期: {dates}")

# 替换
text = "hello   world   python"
clean = re.sub(r"\s+", " ", text)
print(f"清理后: {clean}")

# 分割
parts = re.split(r"[,\s]+", "python, java,go rust")
print(f"分割: {parts}")

# 预编译正则（推荐在循环中使用）
lines = ["name=Tom", "age=18", "city=Beijing"]
pattern = re.compile(r"(\w+)=(\w+)")
for line in lines:
    m = pattern.match(line)
    if m:
        print(f"  {m.group(1)} = {m.group(2)}")

# 命名分组
date_pattern = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})")
m = date_pattern.match("2024-06-15")
if m:
    print(f"年: {m.group('year')}, 月: {m.group('month')}, 日: {m.group('day')}")

# finditer 迭代器
for m in re.finditer(r"\w+", "one two three"):
    print(f"  词: {m.group()}, 位置: {m.start()}-{m.end()}")
