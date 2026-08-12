"""pip install的常见问题"""

# === 常见问题1：权限不足 ===
# pip install flask
# 错误: PermissionError: [Errno 13] Permission denied
#
# 解决方案：
# 1. 使用虚拟环境（推荐）
# 2. pip install --user flask    # 安装到用户目录
# 3. pip install --user flask    # macOS/Linux
#    pip install flask --user    # Windows

# === 常见问题2：网络超时/下载慢 ===
# pip install torch
# 错误: ReadTimeoutError
#
# 解决方案：
# 1. 使用国内镜像源
#    pip install torch -i https://pypi.tuna.tsinghua.edu.cn/simple
# 2. 增加超时时间
#    pip install torch --timeout 300
# 3. 设置全局镜像源
#    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
# 4. 信任非 HTTPS 源（不推荐但有时需要）
#    pip install torch --trusted-host pypi.tuna.tsinghua.edu.cn

print("=== 常见镜像源 ===")
mirrors = {
    "清华": "https://pypi.tuna.tsinghua.edu.cn/simple",
    "阿里": "https://mirrors.aliyun.com/pypi/simple",
    "中科大": "https://pypi.mirrors.ustc.edu.cn/simple",
    "豆瓣": "https://pypi.douban.com/simple",
    "华为": "https://repo.huaweicloud.com/repository/pypi/simple",
}
for name, url in mirrors.items():
    print(f"  {name}: {url}")

# === 常见问题3：版本冲突 ===
# pip install packageA
# 错误: ResolutionImpossibleError / pip's dependency resolver
#
# 原因：packageA 需要 lib==1.0，但已安装 lib==2.0
#
# 解决方案：
# 1. pip install packageA --upgrade   # 尝试升级所有依赖
# 2. pip check                         # 检查依赖冲突
# 3. 创建干净的虚拟环境重新安装
# 4. 指定兼容版本
#    pip install lib==1.0 packageA

print("\n=== pip check 检查依赖 ===")
print("  pip check   # 检查已安装包的依赖是否满足")

# === 常见问题4：编译安装失败 ===
# pip install lxml
# 错误: error: command 'gcc' failed
#
# 原因：某些包需要 C 编译器
#
# 解决方案：
# 1. 安装预编译版本（pip 默认优先选 wheel）
# 2. 安装编译工具
#    macOS:  xcode-select --install
#    Ubuntu: apt install build-essential python3-dev
#    CentOS: yum install gcc python3-devel
# 3. conda install lxml  # connda 优先预编译版本

print("\n=== 编译安装失败处理 ===")
print("  macOS:   xcode-select --install")
print("  Ubuntu:  apt install build-essential python3-dev")
print("  Windows: 安装 Visual C++ Build Tools")

# === 常见问题5：找不到对应版本的 wheel ===
# pip install numpy
# 错误: Could not find a version that satisfies the requirement numpy
#
# 原因：
# 1. Python 版本太新/太旧（如 numpy 不支持 Python 3.12 某些旧版本）
# 2. 平台不匹配（如 ARM macOS 需要原生编译版本）
# 3. 包名拼写错误
#
# 解决方案：
# 1. 检查 Python 版本：python --version
# 2. pip install numpy --only-binary :all:  # 只用预编译版本
# 3. 升级 pip：pip install --upgrade pip
# 4. 检查包名：pip search numpy（如果可用）

# === 常见问题6：pip 本身需要升级 ===
# 错误: You are using pip version 21.x; however, version 23.x is available
# 解决：pip install --upgrade pip
