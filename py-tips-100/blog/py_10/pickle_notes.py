"""pickle序列化的注意事项"""

import pickle
import os


# === pickle 基本用法 ===
data = {
    "name": "Alice",
    "scores": [90, 85, 95],
    "active": True,
    "nested": {"key": "value"},
}

# 序列化到字节
pickled = pickle.dumps(data)
print("pickle字节:", pickled[:50], "...")

# 反序列化
unpickled = pickle.loads(pickled)
print("还原数据:", unpickled)


# === 文件读写 ===
with open("data.pkl", "wb") as f:  # 注意：二进制模式
    pickle.dump(data, f)

with open("data.pkl", "rb") as f:
    loaded = pickle.load(f)
    print("从文件读取:", loaded)

os.remove("data.pkl")


# === pickle vs json 的区别 ===
print("\n=== pickle vs json ===")
comparison = {
    "格式": ("二进制", "文本（JSON）"),
    "可读性": ("不可读", "可读"),
    "支持类型": ("几乎所有Python对象", "基本类型+dict/list"),
    "跨语言": ("否，仅Python", "是，通用格式"),
    "安全性": ("不安全！", "安全"),
    "速度": ("快（C实现）", "稍慢"),
    "文件模式": ("wb/rb 二进制", "w/r 文本"),
}
for feature, (p, j) in comparison.items():
    print(f"  {feature:10s}  pickle: {p:20s}  json: {j}")


# === pickle 支持但 json 不支持的对象 ===
class MyObject:
    def __init__(self, value):
        self.value = value
        self._internal = "secret"

    def __repr__(self):
        return f"MyObject(value={self.value})"


obj = MyObject(42)
# json.dumps(obj)  # TypeError!
pickled_obj = pickle.dumps(obj)  # 可以！
restored = pickle.loads(pickled_obj)
print("\n自定义对象:", restored, restored.value, restored._internal)


# === 安全警告：不要 unpickle 不可信的数据！ ===

# 恶意 pickle 可以执行任意代码
# 错误示例（概念演示，不要实际运行）：
# class Exploit:
#     def __reduce__(self):
#         return (os.system, ("rm -rf /",))
# malicious = pickle.dumps(Exploit())
# pickle.loads(malicious)  # 会执行 os.system("rm -rf /")

print("""
=== 安全规则 ===
1. 永远不要 pickle.loads 来自不受信任来源的数据
2. pickle 适合保存程序自己的中间状态
3. 跨服务/跨语言传输数据用 JSON，不用 pickle
4. 如果必须加载不可信 pickle，用 RestrictedPython 限制
""")


# === 最佳实践 ===
# 1. 保存模型训练状态（如 sklearn 模型）
#    import joblib  # joblib 是 pickle 的增强版，适合大型 numpy 数组
#    joblib.dump(model, "model.joblib")

# 2. 用协议版本提高效率和兼容性
# pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL)

# 3. 大对象用分块或 shelve
import pickle
large_data = list(range(10000))
# protocol=5 支持带偏移的反序列化
pickled5 = pickle.dumps(large_data, protocol=5)
print(f"\nprotocol=5 大小: {len(pickled5)} bytes")
print(f"protocol=4 大小: {len(pickle.dumps(large_data, protocol=4))} bytes")


# === 替代方案 ===
print("""
=== 推荐的替代方案 ===
- 保存数据给其他程序 → JSON / YAML
- 保存 ML 模型 → joblib / ONNX
- 保存 Python 对象状态 → dataclass + JSON
- 需要类型安全 → pydantic + JSON
""")
