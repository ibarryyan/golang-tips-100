"""os和sys模块常用功能示例"""
import os
import sys
from pathlib import Path


def demo_os_path():
    """os路径操作"""
    print("=== os.path ===")
    print(f"  当前目录: {os.getcwd()}")
    print(f"  路径拼接: {os.path.join('a', 'b', 'c')}")
    print(f"  /tmp存在: {os.path.exists('/tmp')}")
    print(f"  dirname: {os.path.dirname('/a/b/c.txt')}")
    print(f"  basename: {os.path.basename('/a/b/c.txt')}")
    print(f"  分割: {os.path.split('/a/b/c.txt')}")
    print(f"  扩展名: {os.path.splitext('/a/b/c.txt')}")


def demo_os_info():
    """os系统信息"""
    print("\n=== os系统信息 ===")
    print(f"  os.name: {os.name}")
    print(f"  cpu_count: {os.cpu_count()}")
    print(f"  pid: {os.getpid()}")
    print(f"  ppid: {os.getppid()}")


def demo_os_file():
    """os文件操作"""
    print("\n=== os文件操作 ===")
    test_dir = "/tmp/py_os_test/subdir"
    os.makedirs(test_dir, exist_ok=True)
    print(f"  创建目录: {test_dir}")

    test_file = os.path.join(test_dir, "test.txt")
    with open(test_file, "w") as f:
        f.write("hello")

    print(f"  文件存在: {os.path.exists(test_file)}")
    print(f"  是文件: {os.path.isfile(test_file)}")
    print(f"  是目录: {os.path.isdir(test_dir)}")
    print(f"  文件大小: {os.path.getsize(test_file)} bytes")

    # 清理
    os.remove(test_file)
    os.removedirs(test_dir)
    print("  已清理")


def demo_sys():
    """sys模块"""
    print("\n=== sys模块 ===")
    print(f"  Python版本: {sys.version}")
    print(f"  平台: {sys.platform}")
    print(f"  编码: {sys.getdefaultencoding()}")
    print(f"  递归限制: {sys.getrecursionlimit()}")
    print(f"  sys.path前3项: {sys.path[:3]}")
    print(f"  argv: {sys.argv}")


def demo_pathlib():
    """推荐：pathlib替代os.path"""
    print("\n=== pathlib（推荐） ===")
    base = Path("/tmp/py_pathlib_test")
    log_file = base / "logs" / "app.log"

    # 创建目录
    log_file.parent.mkdir(parents=True, exist_ok=True)
    print(f"  创建: {log_file.parent}")

    # 读写
    log_file.write_text("Application started\n", encoding="utf-8")
    content = log_file.read_text(encoding="utf-8")
    print(f"  内容: {content.strip()}")

    # 属性
    print(f"  name: {log_file.name}")
    print(f"  suffix: {log_file.suffix}")
    print(f"  parent: {log_file.parent}")
    print(f"  stem: {log_file.stem}")

    # 遍历
    for f in base.rglob("*"):
        print(f"  遍历: {f}")

    # 清理
    log_file.unlink()
    log_file.parent.rmdir()
    base.rmdir()
    print("  已清理")


def demo_argv_parsing():
    """命令行参数简易解析"""
    print("\n=== 命令行参数 ===")
    # 模拟命令行参数
    sys.argv = ["script.py", "--name", "Alice", "--count", "3"]

    # 简易解析
    args = {}
    i = 1
    while i < len(sys.argv):
        if sys.argv[i].startswith("--"):
            key = sys.argv[i][2:]
            value = sys.argv[i + 1] if i + 1 < len(sys.argv) else None
            args[key] = value
            i += 2
        else:
            i += 1

    print(f"  解析结果: {args}")


if __name__ == "__main__":
    demo_os_path()
    demo_os_info()
    demo_os_file()
    demo_sys()
    demo_pathlib()
    demo_argv_parsing()
