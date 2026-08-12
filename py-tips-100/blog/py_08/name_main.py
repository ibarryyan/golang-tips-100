"""__name__ == "__main__"的作用"""


# === 模块可以同时被导入和直接运行 ===

def greet(name):
    print(f"Hello, {name}!")


def main():
    """主入口逻辑"""
    greet("World")
    greet("Python")


# 当直接运行此文件时，__name__ 的值是 "__main__"
# 当被 import 导入时，__name__ 的值是模块名（如 "my_module"）
if __name__ == "__main__":
    main()


# === 为什么需要这个判断？ ===

# 文件 demo_import.py
# import my_module  # 如果没有 if __name__ 判断，导入时会自动执行 main()

# 有了判断后：
# - 直接运行 python my_module.py → 执行 main()
# - 被 import 时 → 只暴露 greet() 函数，不执行 main()


# === 实际项目结构示例 ===
# my_package/
#   __init__.py
#   core.py        # 核心逻辑
#   cli.py         # 命令行入口
#   tests/
#     test_core.py

# core.py
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


# cli.py
def run_cli():
    calc = Calculator()
    print("1 + 2 =", calc.add(1, 2))
    print("3 * 4 =", calc.multiply(3, 4))


if __name__ == "__main__":
    run_cli()


# === 常见用法 ===
# 1. 模块测试代码放在 if __name__ == "__main__" 中
# 2. CLI 入口放在其中
# 3. 脚本可以直接运行，也可以被其他模块安全导入

# === 查看 __name__ 的值 ===
print(f"当前模块 __name__: {__name__}")
# 直接运行时输出: __main__
# 被导入时输出: 模块名（如 name_main_demo）
