"""finally 的执行时机和陷阱"""

# === 陷阱一：finally 中的 return 覆盖 try 中的 return ===
def get_value_bad():
    try:
        return "from try"
    finally:
        return "from finally"  # 这会覆盖 try 的返回值

print("=== 陷阱一：return 覆盖 ===")
print(f"结果: {get_value_bad()}")  # from finally


# === 正确写法：finally 只做清理 ===
def get_value_good():
    try:
        return "from try"
    finally:
        print("finally 执行清理工作")  # 只做清理，不 return

print("\n=== 正确写法 ===")
print(f"结果: {get_value_good()}")


# === 陷阱二：finally 中的异常覆盖 try 中的异常 ===
def risky_bad():
    try:
        1 / 0
    finally:
        raise ValueError("finally 中的异常")  # ZeroDivisionError 被覆盖

print("\n=== 陷阱二：异常覆盖 ===")
try:
    risky_bad()
except Exception as e:
    print(f"捕获到: {type(e).__name__}: {e}")  # 只看到 ValueError


# === 正确写法：finally 不抛异常 ===
def risky_good():
    try:
        1 / 0
    except ZeroDivisionError as e:
        print(f"处理除零错误: {e}")
    finally:
        print("清理资源")  # 只做清理

print("\n=== 正确写法 ===")
risky_good()


# === 正确的资源管理 ===
def read_file_safe(path):
    f = None
    try:
        f = open(path)
        return f.read()
    except FileNotFoundError:
        return "文件不存在"
    finally:
        if f is not None:
            f.close()  # 确保关闭
            print("文件已关闭")

print("\n=== 资源管理 ===")
result = read_file_safe("nonexistent.txt")
print(f"结果: {result}")


# === 推荐使用 with 语句 ===
from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    print(f"获取资源: {name}")
    try:
        yield name
    finally:
        print(f"释放资源: {name}")

print("\n=== with 语句 ===")
with managed_resource("db_connection") as res:
    print(f"使用资源: {res}")
