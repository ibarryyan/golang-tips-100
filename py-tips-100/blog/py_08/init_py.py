"""__init__.py的作用和包结构"""

# === __init__.py 的作用 ===

# 1. 标记一个目录为 Python 包
#    Python 3.3+ 支持隐式命名空间包（不需要 __init__.py）
#    但显式使用 __init__.py 仍然是最清晰、最兼容的做法

# 2. 控制包的公开 API
# 3. 在包被导入时执行初始化代码

# === 示例包结构 ===
# my_package/
#   __init__.py       # 包初始化文件
#   core.py           # 核心模块
#   utils.py          # 工具模块
#   models/
#     __init__.py
#     user.py
#     product.py


# === __init__.py 的常见写法 ===

# 写法1：空文件（仅标记为包）
# __init__.py 为空

# 写法2：暴露子模块的接口
# # my_package/__init__.py
# from .core import Calculator, Engine
# from .utils import helper_function
#
# __all__ = ["Calculator", "Engine", "helper_function"]

# 这样外部可以直接：
# from my_package import Calculator
# 而不需要 from my_package.core import Calculator

# 写法3：设置包级别变量
# # my_package/__init__.py
# __version__ = "1.0.0"
# __author__ = "Alice"


# === 实际演示（模拟包结构）===
import os
import tempfile
import textwrap


def demo_package():
    """创建一个临时包并演示 __init__.py 的作用"""
    tmpdir = tempfile.mkdtemp()

    # 创建包结构
    pkg_dir = os.path.join(tmpdir, "mypkg")
    os.makedirs(pkg_dir)

    # __init__.py
    with open(os.path.join(pkg_dir, "__init__.py"), "w") as f:
        f.write(textwrap.dedent("""\
            from .core import Calculator
            from .utils import format_result

            __version__ = "1.0.0"
            __all__ = ["Calculator", "format_result", "__version__"]
        """))

    # core.py
    with open(os.path.join(pkg_dir, "core.py"), "w") as f:
        f.write(textwrap.dedent("""\
            class Calculator:
                def add(self, a, b):
                    return a + b
        """))

    # utils.py
    with open(os.path.join(pkg_dir, "utils.py"), "w") as f:
        f.write(textwrap.dedent("""\
            def format_result(value):
                return f"结果: {value}"
        """))

    # 导入并使用
    import sys
    sys.path.insert(0, tmpdir)

    from mypkg import Calculator, format_result, __version__

    calc = Calculator()
    result = calc.add(3, 5)
    print(format_result(result))  # 结果: 8
    print("版本:", __version__)   # 1.0.0

    sys.path.remove(tmpdir)
    # 清理
    import shutil
    shutil.rmtree(tmpdir)


demo_package()
