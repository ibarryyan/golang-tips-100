"""json处理中文时的ensure_ascii参数"""

import json


# === 问题：默认 ensure_ascii=True 会转义中文 ===
data = {
    "name": "张三",
    "city": "北京",
    "message": "你好，世界！",
}

# 默认行为：中文被转成 \uXXXX
default_json = json.dumps(data)
print("默认(ensure_ascii=True):")
print(default_json)
# {"name": "\u5f20\u4e09", "city": "\u5317\u4eac", "message": "\u4f60\u597d\uff0c\u4e16\u754c\uff01"}

# 虽然反序列化后是对的，但：
# 1. 文件中不可读
# 2. 占用更多空间
# 3. API 返回时前端需要正确解码（一般没问题但不直观）


# === 解决方案：设置 ensure_ascii=False ===
proper_json = json.dumps(data, ensure_ascii=False)
print("\n修正(ensure_ascii=False):")
print(proper_json)
# {"name": "张三", "city": "北京", "message": "你好，世界！"}


# === 写文件时也要注意 ===
# 错误写法（中文会被转义）
with open("bad.json", "w", encoding="utf-8") as f:
    json.dump(data, f)  # ensure_ascii 默认为 True

# 正确写法
with open("good.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# 读取验证
with open("good.json", "r", encoding="utf-8") as f:
    print("\n读取文件:", json.load(f))

import os
os.remove("bad.json")
os.remove("good.json")


# === 完整的最佳实践 ===
def save_json(data, filepath, indent=2):
    """保存 JSON 文件的标准写法"""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,  # 保留中文明文
            indent=indent,        # 格式化缩进
            sort_keys=False,      # 不自动排序 key（如需排序设 True）
        )


def load_json(filepath):
    """读取 JSON 文件的标准写法"""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


# 测试
save_json(data, "test.json")
print("保存后读取:", load_json("test.json"))
os.remove("test.json")


# === API 开发中的注意事项 ===
# FastAPI / Flask 默认 ensure_ascii=False
# 但如果用 json.dumps 手动构造响应，记得加 ensure_ascii=False

from http.server import HTTPServer, BaseHTTPRequestHandler


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        # 重要：ensure_ascii=False + 指定编码
        response = json.dumps(
            {"message": "你好"},
            ensure_ascii=False
        ).encode("utf-8")
        self.wfile.write(response)


print("\n=== 最佳实践 ===")
print("1. dumps/dump 时始终加 ensure_ascii=False")
print("2. 文件操作指定 encoding='utf-8'")
print("3. HTTP 响应设置 Content-Type 含 charset=utf-8")
print("4. API 框架（FastAPI/Flask）默认已处理好")
