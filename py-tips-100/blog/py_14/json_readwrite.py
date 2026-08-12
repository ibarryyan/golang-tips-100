"""读写 JSON 文件与 jsonl 格式"""

import json
from datetime import datetime

# 写入 JSON
data = {
    "name": "Tom",
    "age": 18,
    "tags": ["python", "go"],
    "address": {"city": "Beijing", "zip": "100000"},
}

json_path = "/tmp/py_json_test.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 读取 JSON
print("=== JSON 读取 ===")
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)
    print(f"  name: {data['name']}")
    print(f"  tags: {data['tags']}")
    print(f"  city: {data['address']['city']}")

# 字符串与 JSON 互转
json_str = json.dumps(data, ensure_ascii=False)
data_back = json.loads(json_str)
print(f"\n字符串互转: {data_back['name']}")

# JSONL 格式（每行一个 JSON 对象）
jsonl_path = "/tmp/py_jsonl_test.jsonl"
records = [
    {"id": 1, "name": "Tom", "score": 90},
    {"id": 2, "name": "Jerry", "score": 85},
    {"id": 3, "name": "Spike", "score": 95},
]

with open(jsonl_path, "w", encoding="utf-8") as f:
    for record in records:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

print("\n=== JSONL 读取 ===")
with open(jsonl_path, "r", encoding="utf-8") as f:
    for line in f:
        record = json.loads(line.strip())
        print(f"  id={record['id']}, name={record['name']}, score={record['score']}")

# 处理特殊类型——日期时间
def json_default(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"无法序列化 {type(obj)}")

dt = datetime.now()
result = json.dumps({"time": dt}, default=json_default, ensure_ascii=False)
print(f"\n日期序列化: {result}")

# 清理
import os
os.remove(json_path)
os.remove(jsonl_path)
