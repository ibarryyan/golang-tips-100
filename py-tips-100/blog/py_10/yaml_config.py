"""yaml配置文件读取"""

# YAML 比 JSON 更适合写配置文件：
# - 支持注释
# - 缩进表示层级（不能用 Tab，只能用空格）
# - 支持多行字符串、锚点引用等高级特性

import json

# 先安装 PyYAML: pip install pyyaml
try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    print("PyYAML 未安装，请运行: pip install pyyaml")
    print("以下是 YAML 的语法说明和用法演示\n")


# === YAML 示例配置 ===
yaml_config = """
# 应用配置
app:
  name: MyAIApp
  version: 1.0.0
  debug: true
  port: 8080

# 数据库配置
database:
  host: localhost
  port: 5432
  name: mydb
  user: admin
  password: secret123
  pool_size: 10

# 模型配置
models:
  - name: gpt-4
    max_tokens: 8192
    temperature: 0.7
  - name: claude-3
    max_tokens: 4096
    temperature: 0.5

# 多行字符串（两种方式）
description: |
  这是一个AI应用
  支持多行配置说明

# 单行长文本
prompt: >
  你是一个助手，
  请帮助用户解决问题。

# 布尔值和 null
features:
  cache: true
  logging: false
  experimental: null

# 锚点和引用（避免重复）
default_model: &default
  temperature: 0.7
  top_p: 0.9

models_ref:
  production:
    <<: *default
    name: gpt-4
  dev:
    <<: *default
    name: gpt-3.5
    temperature: 0.3  # 覆盖默认值
"""

if HAS_YAML:
    # === 读取 YAML ===
    config = yaml.safe_load(yaml_config)
    print("YAML 解析结果:")
    print(json.dumps(config, indent=2, ensure_ascii=False))

    # === 访问配置 ===
    print("\napp.name:", config["app"]["name"])
    print("database.host:", config["database"]["host"])
    print("models数量:", len(config["models"]))

    # === 写入 YAML ===
    yaml_output = yaml.dump(config, allow_unicode=True, default_flow_style=False, sort_keys=False)
    print("\nYAML 输出（部分）:")
    print(yaml_output[:200] + "...")

    # === 安全 vs 非安全 ===
    # safe_load：只解析基本类型，不执行任意 Python 对象（推荐）
    # load / unsafe_load：可能执行恶意代码（不要用！）
    # yaml.load(data, Loader=yaml.SafeLoader)  # 等同于 safe_load

    # === 文件读写 ===
    import tempfile
    import os

    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False, encoding="utf-8") as f:
        yaml.dump(config, f, allow_unicode=True, default_flow_style=False)
        yaml_path = f.name

    with open(yaml_path, "r", encoding="utf-8") as f:
        loaded_config = yaml.safe_load(f)
    print("\n从文件读取:", loaded_config["app"]["name"])

    os.remove(yaml_path)

else:
    print(yaml_config)
    print("(以上为 YAML 语法示例，安装 PyYAML 后可直接解析)")
