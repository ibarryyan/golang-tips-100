"""requirements.txt和pip freeze"""

import subprocess
import sys


def demo_pip_freeze():
    """演示 pip freeze 和 requirements.txt 的使用"""

    # === pip freeze：导出当前环境所有已安装的包 ===
    result = subprocess.run(
        [sys.executable, "-m", "pip", "freeze"],
        capture_output=True, text=True
    )

    # 取前几个包作为示例
    lines = result.stdout.strip().split("\n")[:5]
    print("pip freeze 输出示例:")
    for line in lines:
        print(f"  {line}")

    # === requirements.txt 格式 ===
    print("""
# requirements.txt 常见格式：

# 精确版本（生产环境推荐）
flask==2.3.3
requests==2.31.0
numpy==1.24.3

# 版本范围（开发环境可用）
django>=4.0,<5.0
celery>=5.2,<6.0

# 从指定源安装
--index-url https://pypi.org/simple/
--extra-index-url https://download.pytorch.org/whl/cu118
torch==2.0.1

# 从 Git 仓库安装
git+https://github.com/psf/requests.git@main

# 从本地路径安装
./my-local-package
# -e ../editable-package  # 可编辑模式

# 包含可选依赖
celery[redis]==5.2.7
uvicorn[standard]==0.23.2

# 通过文件引入其他依赖
-r requirements-extra.txt
""")

    # === 生成 requirements.txt ===
    # 方法1：直接 freeze
    # pip freeze > requirements.txt

    # 方法2：手动维护（推荐）
    # 只写顶层依赖，让 pip 自动解决子依赖
    # pip install pip-tools
    # pip-compile  # 生成 requirements.txt（锁定所有版本）

    # === 安装依赖 ===
    # pip install -r requirements.txt
    # pip install -r requirements.txt --upgrade
    # pip install -r requirements.txt --no-deps  # 只装指定包，不装依赖

    # === 最佳实践 ===
    # 1. 项目根目录放 requirements.txt
    # 2. 区分开发和生产依赖：
    #    requirements.txt       # 生产
    #    requirements-dev.txt  # 开发（包含测试、lint 等工具）
    # 3. 用 pip-compile 精确锁定版本
    # 4. 每次 pip install 后及时更新 requirements.txt


def show_installed_packages():
    """查看已安装的包"""
    result = subprocess.run(
        [sys.executable, "-m", "pip", "list", "--format=columns"],
        capture_output=True, text=True
    )
    lines = result.stdout.strip().split("\n")[:6]
    print("pip list 示例:")
    for line in lines:
        print(f"  {line}")


show_installed_packages()
demo_pip_freeze()
