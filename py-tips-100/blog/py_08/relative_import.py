"""相对导入和绝对导入"""

# === 绝对导入：从包的顶层开始 ===

# 语法：from package.subpackage.module import name
# 优点：清晰明确，IDE 自动补全好
# 缺点：包名改变时需要修改所有导入

# 示例：
# from my_package.core import Calculator
# from my_package.utils import helper_function
# from my_package.models.user import User


# === 相对导入：用 . 表示当前包，.. 表示父包 ===

# 语法：
#   from .module import name        # 当前包内的模块
#   from .module import name as alias
#   from ..sibling import name      # 上一级包的模块
#   from . import module            # 导入整个模块

# 优点：包内重构时不用改导入路径
# 缺点：不能直接运行单个模块文件（会报错）


# === 实际示例（模拟包结构）===
# project/
#   __init__.py
#   core/
#     __init__.py
#     engine.py       # from ..utils import helper
#     calculator.py    # from .engine import Engine
#   utils/
#     __init__.py
#     helpers.py


# === 相对导入的常见错误 ===

# 错误：直接运行包内的模块文件
# python project/core/calculator.py
# 报错：ImportError: attempted relative import with no known parent package

# 正确：用 python -m 运行
# python -m project.core.calculator

# 或者从外部脚本导入


# === 演示 ===
import os
import tempfile
import textwrap
import sys


def demo_relative_import():
    """演示相对导入"""
    tmpdir = tempfile.mkdtemp()

    # 创建包结构
    pkg = os.path.join(tmpdir, "project")
    os.makedirs(os.path.join(pkg, "core"))
    os.makedirs(os.path.join(pkg, "utils"))

    # project/__init__.py
    open(os.path.join(pkg, "__init__.py"), "w").close()

    # project/utils/__init__.py
    with open(os.path.join(pkg, "utils", "__init__.py"), "w") as f:
        f.write("from .helpers import helper\n")

    # project/utils/helpers.py
    with open(os.path.join(pkg, "utils", "helpers.py"), "w") as f:
        f.write("def helper():\n    return 'I am helper'\n")

    # project/core/__init__.py
    open(os.path.join(pkg, "core", "__init__.py"), "w").close()

    # project/core/engine.py - 使用相对导入
    with open(os.path.join(pkg, "core", "engine.py"), "w") as f:
        f.write(textwrap.dedent("""\
            from ..utils import helper  # 相对导入：上一级包的 utils

            class Engine:
                def run(self):
                    return helper()
        """))

    sys.path.insert(0, tmpdir)

    # 绝对导入
    from project.core.engine import Engine
    engine = Engine()
    print("相对导入结果:", engine.run())  # I am helper

    sys.path.remove(tmpdir)
    import shutil
    shutil.rmtree(tmpdir)


demo_relative_import()

# === 最佳实践 ===
# 1. 项目对外提供的包用绝对导入
# 2. 包内部的模块间用相对导入
# 3. 永远不要直接 python xxx.py 运行包内模块，用 python -m
