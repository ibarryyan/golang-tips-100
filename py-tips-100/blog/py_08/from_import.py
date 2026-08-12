"""from import和import的区别"""

# === import 模块 ===
import math

# 使用时需要加模块名前缀
print("math.pi:", math.pi)
print("math.sqrt(16):", math.sqrt(16))
print()

# 优点：命名空间清晰，不会命名冲突
# 缺点：每次访问要加前缀


# === from import 导入特定对象 ===
from math import pi, sqrt

# 直接使用，不需要前缀
print("pi:", pi)
print("sqrt(16):", sqrt(16))

# 优点：代码简洁
# 缺点：如果导入太多，可能命名冲突


# === from import * 导入全部（不推荐）===
# from math import *  # 污染命名空间，不知道哪些是导入的

# 问题示例：
# from math import *
# from os import *
# 两个模块可能有同名函数，后导入的会覆盖前面的


# === import as 别名 ===
# 常见缩写约定：import numpy as np / import pandas as pd
from math import sqrt as square_root

print("import as 别名:", square_root(9))
# 如果安装了 numpy：
# import numpy as np
# print("np.array:", np.array([1, 2, 3]))


# === 导入自定义模块 ===
# 假设项目结构：
# project/
#   utils/
#     string_tools.py
#     file_tools.py
#   main.py

# 在 main.py 中：
# 方式1：import 模块
#   import utils.string_tools
#   utils.string_tools.capitalize("hello")

# 方式2：from import 具体函数
#   from utils.string_tools import capitalize
#   capitalize("hello")

# 方式3：from import 模块
#   from utils import string_tools
#   string_tools.capitalize("hello")


# === 性能差异 ===
# import 和 from import 在性能上几乎没有区别
# 都是执行模块的顶层代码，创建模块对象

# 选择建议：
# 1. 标准库用 import（如 import os, import sys）
# 2. 具体函数用 from import（如 from collections import defaultdict）
# 3. 第三方库用 import as 别名（如 import numpy as np）
# 4. 永远不要用 from xxx import *


# === 导入顺序约定（PEP 8）===
# 1. 标准库
# 2. 第三方库
# 3. 本地模块
# 每组之间用空行分隔
