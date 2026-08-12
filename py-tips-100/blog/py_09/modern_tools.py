"""uv/poetry等现代依赖管理工具"""

# === uv：极速依赖管理（Rust 编写） ===
# 安装：pip install uv 或 curl -LsSf https://astral.sh/uv/install.sh | sh
#
# 特点：比 pip 快 10-100 倍，一个工具搞定 venv + pip + pip-tools
#
# 常用命令：
#   uv venv                    # 创建虚拟环境
#   uv pip install flask       # 安装包（兼容 pip 语法）
#   uv pip install -r requirements.txt  # 从 requirements 安装
#   uv pip freeze              # 导出已安装包
#   uv pip compile             # 生成 lock 文件
#
# 项目管理（uv >= 0.3.0）：
#   uv init my-project         # 初始化新项目
#   uv add flask               # 添加依赖
#   uv add --dev pytest        # 添加开发依赖
#   uv remove flask            # 移除依赖
#   uv sync                    # 同步安装所有依赖
#   uv lock                    # 生成/更新 lock 文件
#   uv run python main.py      # 在项目环境中运行

print("=== uv 常用命令 ===")
uv_commands = {
    "uv venv": "创建虚拟环境",
    "uv add flask": "添加依赖到项目",
    "uv add --dev pytest": "添加开发依赖",
    "uv sync": "同步安装所有依赖（根据 lock 文件）",
    "uv lock": "生成/更新 uv.lock",
    "uv run python main.py": "在项目环境中运行命令",
    "uv pip install flask": "兼容 pip 语法安装包",
    "uv tool install ruff": "安装 CLI 工具",
}
for cmd, desc in uv_commands.items():
    print(f"  {cmd:40s} {desc}")


# === poetry：成熟的依赖管理 + 打包工具 ===
# 安装：pip install poetry 或 curl -sSL https://install.python-poetry.org | python3 -
#
# 特点：pyproject.toml 管理依赖，poetry.lock 锁定版本，支持发布到 PyPI
#
# 常用命令：
#   poetry init              # 交互式初始化项目
#   poetry new my-project    # 创建标准项目结构
#   poetry add flask         # 添加依赖
#   poetry add --group dev pytest  # 添加开发依赖
#   poetry remove flask      # 移除依赖
#   poetry install           # 安装所有依赖
#   poetry lock              # 生成/更新 lock 文件
#   poetry run python main.py  # 在虚拟环境中运行
#   poetry shell             # 激活虚拟环境
#   poetry build             # 打包（sdist + wheel）
#   poetry publish           # 发布到 PyPI

print("\n=== poetry 常用命令 ===")
poetry_commands = {
    "poetry new my-project": "创建标准项目结构",
    "poetry init": "交互式初始化已有项目",
    "poetry add flask": "添加依赖",
    "poetry add --group dev pytest": "添加开发依赖",
    "poetry install": "安装所有依赖",
    "poetry lock": "生成/更新 poetry.lock",
    "poetry run python main.py": "在虚拟环境中运行",
    "poetry shell": "激活虚拟环境",
    "poetry build": "打包项目",
    "poetry publish": "发布到 PyPI",
}
for cmd, desc in poetry_commands.items():
    print(f"  {cmd:40s} {desc}")


# === pyproject.toml 示例 ===
print("""
=== pyproject.toml 示例 ===

[project]
name = "my-project"
version = "0.1.0"
description = "My Python project"
requires-python = ">=3.10"
dependencies = [
    "flask>=3.0",
    "requests>=2.31",
]

[project.optional-dependencies]
dev = ["pytest>=7.0", "ruff>=0.1"]

[tool.uv]
# uv 专用配置

[tool.poetry]
# poetry 专用配置
""")


# === 其他工具简述 ===
print("=== 其他工具 ===")
tools = {
    "pipenv": "Pipfile + Pipfile.lock，早期集成方案，社区活跃度下降",
    "conda/mamba": "科学计算首选，管理非 Python 依赖（如 CUDA）",
    "rye": "Rust 实现的轻量项目管理，类似 uv 的定位",
    "hatch": "可扩展的项目管理工具，PEP 621 标准支持",
    "pdm": "PEP 582 标准，不依赖虚拟环境",
}
for name, desc in tools.items():
    print(f"  {name:15s} {desc}")


# === 选择建议 ===
print("""
=== 选择建议 ===
1. 简单脚本：venv + pip + requirements.txt
2. 新项目（2024+）：uv（最快，生态整合最好）
3. 库开发：poetry 或 hatch（成熟，发布流程完善）
4. 科学计算：conda/mamba（管理 CUDA 等非 Python 依赖）
5. 已有 poetry 项目：继续用 poetry，也可迁移到 uv
""")
