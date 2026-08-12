"""cProfile 分析性能瓶颈演示"""
import cProfile
import pstats
import io


def slow_function():
    """模拟慢函数"""
    total = 0
    for i in range(10000):
        total += sum(x * x for x in range(100))
    return total


def fast_function():
    """模拟快函数"""
    return sum(x * x for x in range(100)) * 10000


def medium_function():
    """中等速度函数"""
    result = []
    for i in range(1000):
        result.append(sum(range(50)))
    return result


def main():
    slow_function()
    medium_function()
    fast_function()


def demo_basic_profile():
    """基本性能分析"""
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()

    stats = pstats.Stats(profiler)
    stats.sort_stats("cumulative")
    print("--- 按累计耗时排序 ---")
    stats.print_stats(10)


def demo_tottime_sort():
    """按函数自身耗时排序"""
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()

    stats = pstats.Stats(profiler)
    stats.sort_stats("tottime")
    print("\n--- 按函数自身耗时排序 ---")
    stats.print_stats(10)


def demo_string_output():
    """输出到字符串"""
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()

    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream)
    stats.sort_stats("cumulative")
    stats.print_stats(5)

    output = stream.getvalue()
    lines = output.strip().split("\n")
    for line in lines[:8]:
        print(line)


if __name__ == "__main__":
    print("=== 基本性能分析 ===")
    demo_basic_profile()

    print("\n=== 按函数自身耗时排序 ===")
    demo_tottime_sort()

    print("\n=== 输出到字符串 ===")
    demo_string_output()

    print("\n命令行用法:")
    print("  python -m cProfile -s cumulative cprofile_demo.py")
    print("  python -m cProfile -s tottime cprofile_demo.py")
