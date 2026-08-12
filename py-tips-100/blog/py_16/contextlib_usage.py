"""contextlib 实现上下文管理器"""

import os
import time
from contextlib import contextmanager, suppress, ExitStack


# === 传统写法：手写类 ===
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.time() - self.start
        print(f"耗时: {self.elapsed:.3f}s")
        return False  # 不抑制异常


# === 推荐写法：@contextmanager ===
@contextmanager
def timer(label: str = "操作"):
    start = time.time()
    try:
        yield  # yield 之前是 __enter__，之后是 __exit__
    finally:
        elapsed = time.time() - start
        print(f"{label} 耗时: {elapsed:.3f}s")


print("=== @contextmanager ===")
with timer("计算"):
    sum(range(1000000))


# === 实际应用：原子写入 ===
@contextmanager
def atomic_write(filepath, mode="w", encoding="utf-8"):
    """原子写入：先写临时文件，成功后重命名"""
    tmp = filepath + ".tmp"
    try:
        with open(tmp, mode, encoding=encoding) as f:
            yield f
            f.flush()
            os.fsync(f.fileno())
        os.rename(tmp, filepath)
        print(f"写入成功: {filepath}")
    except Exception:
        if os.path.exists(tmp):
            os.remove(tmp)
        print(f"写入失败，清理临时文件")
        raise


print("\n=== 原子写入 ===")
test_file = "/tmp/py_context_test.txt"
with atomic_write(test_file) as f:
    f.write('{"status": "ok"}')
print(f"文件内容: {os.popen('cat ' + test_file).read().strip()}")
os.remove(test_file)


# === suppress: 静默忽略异常 ===
print("\n=== suppress ===")
# 错误示例
try:
    os.remove("nonexistent_file.txt")
except FileNotFoundError:
    pass

# 推荐写法
with suppress(FileNotFoundError):
    os.remove("nonexistent_file.txt")

print("suppress 静默忽略了 FileNotFoundError")


# === ExitStack: 管理多个上下文 ===
print("\n=== ExitStack ===")
files_data = ["文件A内容", "文件B内容", "文件C内容"]
file_paths = [f"/tmp/py_stack_{i}.txt" for i in range(3)]

# 创建测试文件
for path, data in zip(file_paths, files_data):
    with open(path, "w") as f:
        f.write(data)

# 用 ExitStack 同时管理多个文件
with ExitStack() as stack:
    handles = [stack.enter_context(open(f)) for f in file_paths]
    for h in handles:
        print(f"  读取: {h.read().strip()}")

# 清理
for path in file_paths:
    os.remove(path)

print("所有文件已关闭并清理")
