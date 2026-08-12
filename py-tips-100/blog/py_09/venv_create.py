"""venv创建和激活虚拟环境"""

import subprocess
import os
import sys
import tempfile


def demo_venv():
    """演示创建虚拟环境的完整过程"""

    # === 创建虚拟环境 ===
    # 命令行执行（Python 3.3+ 自带 venv 模块）
    # python -m venv myenv

    venv_dir = os.path.join(tempfile.mkdtemp(), "myenv")

    # 在代码中创建虚拟环境
    result = subprocess.run(
        [sys.executable, "-m", "venv", venv_dir],
        capture_output=True, text=True
    )

    if result.returncode != 0:
        print("创建失败:", result.stderr)
        return

    print("虚拟环境创建成功:", venv_dir)

    # === 虚拟环境结构 ===
    # Windows:
    #   myenv/
    #     Scripts/      # 激活脚本和 python.exe
    #       activate.bat
    #       activate.ps1
    #       python.exe
    #     Lib/          # 安装的包
    #     pyvenv.cfg

    # macOS/Linux:
    #   myenv/
    #     bin/          # 激活脚本和 python
    #       activate
    #       activate.fish
    #       python
    #       pip
    #     lib/          # 安装的包
    #     pyvenv.cfg    # 配置信息

    # === 激活方式 ===
    # macOS/Linux:
    #   source myenv/bin/activate
    #
    # Windows (cmd):
    #   myenv\\Scripts\\activate.bat
    #
    # Windows (PowerShell):
    #   myenv\\Scripts\\Activate.ps1
    #
    # 退出虚拟环境:
    #   deactivate

    # === 检查虚拟环境 ===
    pyvenv_cfg = os.path.join(venv_dir, "pyvenv.cfg")
    if os.path.exists(pyvenv_cfg):
        with open(pyvenv_cfg, "r") as f:
            print("\npyvenv.cfg 内容:")
            print(f.read())

    # === 为什么需要虚拟环境？ ===
    # 1. 项目隔离：不同项目依赖不同版本的包
    #    项目A需要 Django 3.x，项目B需要 Django 4.x
    # 2. 避免污染系统 Python
    # 3. 可复现环境：通过 requirements.txt 精确记录依赖
    # 4. 不同 Python 版本测试

    # === 常用 venv 参数 ===
    # --system-site-packages  允许访问系统已安装的包
    # --copies                复制而非符号链接（某些系统更稳定）
    # --without-pip            不安装 pip（需要手动安装）

    # 清理
    import shutil
    shutil.rmtree(os.path.dirname(venv_dir))


demo_venv()


# === 一行创建 + 激活（shell 脚本风格）===
print("""
# 完整工作流：
python -m venv .venv          # 创建
source .venv/bin/activate     # 激活（macOS/Linux）
# .venv\\Scripts\\activate     # 激活（Windows）
pip install -r requirements.txt  # 安装依赖
python main.py                # 运行项目
deactivate                    # 退出
""")
