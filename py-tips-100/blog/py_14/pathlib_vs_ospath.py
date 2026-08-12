"""os.path vs pathlib 选择对比"""

import os.path
from pathlib import Path

# 传统 os.path 写法
path = os.path.join("data", "input", "test.txt")
print("=== os.path ===")
print(f"路径: {path}")
print(f"父目录: {os.path.dirname(path)}")
print(f"文件名: {os.path.basename(path)}")
name, ext = os.path.splitext(os.path.basename(path))
print(f"stem: {name}, suffix: {ext}")
print(f"存在: {os.path.exists(path)}")

# 现代 pathlib 写法（推荐）
p = Path("data") / "input" / "test.txt"
print("\n=== pathlib ===")
print(f"路径: {p}")
print(f"父目录: {p.parent}")
print(f"文件名: {p.name}")
print(f"stem: {p.stem}")
print(f"suffix: {p.suffix}")
print(f"suffixes: {p.suffixes}")

# pathlib 链式调用
print("\n=== pathlib 高级用法 ===")
# 创建目录
Path("/tmp/py_test_dir").mkdir(parents=True, exist_ok=True)

# 写入和读取
p_write = Path("/tmp/py_test_dir/hello.txt")
p_write.write_text("hello pathlib", encoding="utf-8")
print(f"读取: {p_write.read_text(encoding='utf-8')}")

# 遍历目录
print("\n遍历 /tmp/py_test_dir:")
for f in Path("/tmp/py_test_dir").iterdir():
    print(f"  {f.name} (file={f.is_file()})")

# 清理
p_write.unlink()
Path("/tmp/py_test_dir").rmdir()
