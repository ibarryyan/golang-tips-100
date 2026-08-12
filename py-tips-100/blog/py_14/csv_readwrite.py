"""读写 CSV 文件"""

import csv

# 写入 CSV
data = [
    ["name", "age", "city"],
    ["Tom", 18, "Beijing"],
    ["Jerry", 25, "Shanghai"],
]

csv_path = "/tmp/py_csv_test.csv"
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# 读取 CSV
print("=== csv.reader ===")
with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"  {row}")

# 使用 DictWriter
dict_csv_path = "/tmp/py_dict_csv.csv"
users = [
    {"name": "Tom", "age": "18", "city": "Beijing"},
    {"name": "Jerry", "age": "25", "city": "Shanghai"},
    {"name": "Spike", "age": "30", "city": "Guangzhou"},
]

with open(dict_csv_path, "w", newline="", encoding="utf-8") as f:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(users)

# 使用 DictReader
print("\n=== csv.DictReader ===")
with open(dict_csv_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['name']}, {row['age']}, {row['city']}")

# 清理
import os
os.remove(csv_path)
os.remove(dict_csv_path)
