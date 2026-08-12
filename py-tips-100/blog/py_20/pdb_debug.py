"""pdb 调试技巧演示"""
import sys


def calculate(x, y):
    """演示用 breakpoint() 调试"""
    result = x * 2 + y
    # Python 3.7+ 内置 breakpoint()
    # 程序运行到这里会暂停，进入交互式调试
    # 取消下面这行的注释来体验调试：
    # breakpoint()
    result = result ** 2
    return result


def complex_logic(data):
    """多步逻辑，适合断点调试"""
    step1 = [x * 2 for x in data]
    step2 = [x for x in step1 if x > 5]
    step3 = sum(step2)
    return step3


def demonstrate_pdb_commands():
    """展示 pdb 常用命令（注释形式说明）"""
    data = [1, 3, 5, 7, 9]

    # 设置断点后，可以在 pdb 中执行：
    # n (next)      - 执行下一行，不进入函数
    # s (step)      - 执行下一行，进入函数
    # c (continue)  - 继续到下一个断点
    # p data        - 打印变量 data
    # pp data       - pretty print 变量
    # l (list)      - 查看当前代码上下文
    # w (where)     - 查看调用栈
    # u (up)        - 上移调用栈
    # d (down)      - 下移调用栈
    # b 20          - 在第 20 行设置断点
    # q (quit)      - 退出调试器

    result = complex_logic(data)
    print(f"结果: {result}")


if __name__ == "__main__":
    print("=== 基础计算 ===")
    print(f"calculate(3, 4) = {calculate(3, 4)}")

    print("\n=== 复杂逻辑 ===")
    demonstrate_pdb_commands()

    print("\n=== pdb 使用说明 ===")
    print("1. 在代码中插入 breakpoint() 即可暂停")
    print("2. 命令行运行: python -m pdb pdb_debug.py")
    print("3. 安装 ipdb: pip install ipdb")
    print("4. 设置环境变量: export PYTHONBREAKPOINT=ipdb.set_trace")
