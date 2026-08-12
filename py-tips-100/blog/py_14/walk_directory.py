"""递归遍历目录树"""

import os
from pathlib import Path

# 创建测试目录结构
test_dir = Path("/tmp/py_walk_test")
test_dir.mkdir(parents=True, exist_ok=True)
(test_dir / "a.py").write_text("print('a')")
(test_dir / "sub1").mkdir(exist_ok=True)
(test_dir / "sub1" / "b.py").write_text("print('b')")
(test_dir / "sub1" / "sub2").mkdir(exist_ok=True)
(test_dir / "sub1" / "sub2" / "c.py").write_text("print('c')")
(test_dir / "data.txt").write_text("data")

print("=== os.walk ===")
for dirpath, dirnames, filenames in os.walk(test_dir):
    # 跳过 .git 目录（演示修改 dirnames）
    if ".git" in dirnames:
        dirnames.remove(".git")
    for f in filenames:
        if f.endswith(".py"):
            filepath = os.path.join(dirpath, f)
            print(f"  {filepath}")

print("\n=== pathlib.rglob ===")
for py_file in test_dir.rglob("*.py"):
    print(f"  {py_file}")

print("\n=== 获取文件信息 ===")
for py_file in test_dir.rglob("*.py"):
    stat = py_file.stat()
    print(f"  {py_file.name}: {stat.st_size} bytes")

# 友好的文件大小
def human_size(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} PB"

print("\n=== 文件大小 ===")
for py_file in test_dir.rglob("*"):
    if py_file.is_file():
        print(f"  {py_file.name}: {human_size(py_file.stat().st_size)}")

# 清理
import shutil
shutil.rmtree(test_dir)
