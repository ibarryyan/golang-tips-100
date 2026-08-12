"""json模块的序列化和反序列化"""

import json
from dataclasses import dataclass, asdict
from datetime import datetime
from enum import Enum


# === 基本用法 ===
data = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "Go", "SQL"],
    "active": True,
    "score": 95.5,
    "address": None,
}

# 序列化：dict → json 字符串
json_str = json.dumps(data)
print("JSON字符串:", json_str)

# 反序列化：json 字符串 → dict
parsed = json.loads(json_str)
print("解析回来:", parsed)
print("类型:", type(parsed))  # <class 'dict'>


# === 文件读写 ===
# 写入 JSON 文件
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# 读取 JSON 文件
with open("output.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print("\n从文件读取:", loaded)

import os
os.remove("output.json")


# === JSON 支持的数据类型 ===
# ✅ str, int, float, bool, None, list, dict
# ❌ tuple → 变成 list
# ❌ set, bytes, datetime, 自定义对象 → 报错

# tuple 会被转成 list
data_tuple = {"items": (1, 2, 3)}
print("\ntuple变成:", json.loads(json.dumps(data_tuple)))  # {'items': [1, 2, 3]}

# 自定义对象需要转换
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {"name": self.name, "age": self.age}


user = User("Bob", 25)
# json.dumps(user)  # TypeError!
print("手动转dict:", json.dumps(user.to_dict()))


# === 使用 dataclass 更优雅地处理 ===
@dataclass
class Product:
    name: str
    price: float
    tags: list


product = Product("Laptop", 999.99, ["electronics", "portable"])
# dataclass 转 dict 再转 JSON
product_json = json.dumps(asdict(product))
print("dataclass转JSON:", product_json)


# === 不支持的类型需要自定义编码器 ===
class CustomEncoder(json.JSONEncoder):
    """自定义 JSON 编码器"""
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, Enum):
            return obj.value
        return super().default(obj)


data_with_dt = {"created_at": datetime(2025, 1, 15, 10, 30)}
print("自定义编码器:", json.dumps(data_with_dt, cls=CustomEncoder))


# === 反序列化时恢复类型 ===
def parse_datetime(dct):
    """自定义解码钩子"""
    for key, value in dct.items():
        if key.endswith("_at") and isinstance(value, str):
            try:
                dct[key] = datetime.fromisoformat(value)
            except ValueError:
                pass
    return dct


json_str = '{"created_at": "2025-01-15T10:30:00"}'
result = json.loads(json_str, object_hook=parse_datetime)
print("自定义解码:", result, type(result["created_at"]))
