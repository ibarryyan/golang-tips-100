"""raise from 异常链的用法"""

import urllib.request
import urllib.error


# === 不使用异常链（丢失原始信息） ===
def read_config_bad(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        raise RuntimeError("配置文件读取失败")  # 原始异常丢失


# === 使用 raise from（推荐） ===
def read_config(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError as e:
        raise RuntimeError("配置文件读取失败") from e  # 保留异常链


# === raise from None: 抑制原始异常 ===
def parse_user(data):
    try:
        return {"name": data["name"], "age": int(data["age"])}
    except (KeyError, ValueError):
        raise ValueError("用户数据格式错误") from None


# === 实际应用：异常转换模式 ===
class ServiceError(Exception):
    pass


def call_api(url):
    try:
        response = urllib.request.urlopen(url, timeout=5)
        return response.read()
    except urllib.error.URLError as e:
        raise ServiceError(f"API 调用失败: {url}") from e


# 测试异常链
print("=== raise from 保留异常链 ===")
try:
    read_config("nonexistent_config.txt")
except RuntimeError as e:
    print(f"捕获: {e}")
    print(f"原始异常: {e.__cause__}")

print("\n=== raise from None 抑制异常 ===")
try:
    parse_user({"name": "Tom"})  # 缺少 age
except ValueError as e:
    print(f"捕获: {e}")
    print(f"原始异常: {e.__cause__}")  # None

print("\n=== 异常转换模式 ===")
try:
    call_api("http://nonexistent.example.com")
except ServiceError as e:
    print(f"捕获: {e}")
    print(f"原始异常: {e.__cause__}")
