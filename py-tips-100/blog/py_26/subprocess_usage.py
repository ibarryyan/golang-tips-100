"""subprocess执行外部命令示例"""
import subprocess
from typing import Optional


def basic_run():
    """基础用法"""
    print("=== 基础用法 ===")
    result = subprocess.run(
        ["echo", "Hello, subprocess!"],
        capture_output=True,
        text=True
    )
    print(f"  输出: {result.stdout.strip()}")
    print(f"  返回码: {result.returncode}")


def run_with_check():
    """check参数"""
    print("\n=== check参数 ===")
    try:
        result = subprocess.run(
            ["ls", "/nonexistent_path"],
            capture_output=True,
            text=True,
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"  命令失败: 返回码={e.returncode}")
        print(f"  错误信息: {e.stderr.strip()}")


def safe_run(cmd: list[str], timeout: int = 30) -> Optional[str]:
    """封装安全命令执行"""
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"  [错误] 命令失败: {' '.join(cmd)}")
        print(f"  [错误] stderr: {e.stderr.strip()}")
        return None
    except subprocess.TimeoutExpired:
        print(f"  [超时] 命令超时: {' '.join(cmd)}")
        return None


def demo_safe_run():
    """演示安全执行"""
    print("\n=== 安全执行 ===")
    output = safe_run(["echo", "safe run works"])
    print(f"  结果: {output}")

    output = safe_run(["ls", "/nonexistent"])
    print(f"  失败结果: {output}")


def pipe_commands():
    """管道操作"""
    print("\n=== 管道操作 ===")
    # 方法1：Popen + 管道
    p1 = subprocess.Popen(
        ["echo", "line1\nline2\nline3"],
        stdout=subprocess.PIPE
    )
    p2 = subprocess.Popen(
        ["grep", "line2"],
        stdin=p1.stdout,
        stdout=subprocess.PIPE,
        text=True
    )
    p1.stdout.close()
    output = p2.communicate()[0]
    print(f"  管道输出: {output.strip()}")

    # 方法2：shell管道（仅用于简单场景，不处理用户输入时）
    result = subprocess.run(
        "echo 'hello world' | tr 'a-z' 'A-Z'",
        shell=True,
        capture_output=True,
        text=True
    )
    print(f"  shell管道: {result.stdout.strip()}")


def demo_timeout():
    """超时控制"""
    print("\n=== 超时控制 ===")
    try:
        result = subprocess.run(
            ["sleep", "10"],
            timeout=2,
            capture_output=True
        )
    except subprocess.TimeoutExpired:
        print("  命令在2秒后被终止")


def get_system_info():
    """实用：获取系统信息"""
    print("\n=== 系统信息 ===")
    # 当前目录文件列表
    files = safe_run(["ls", "-la", "/tmp"])
    if files:
        for line in files.split("\n")[:5]:
            print(f"  {line}")


if __name__ == "__main__":
    basic_run()
    run_with_check()
    demo_safe_run()
    pipe_commands()
    demo_timeout()
    get_system_info()
