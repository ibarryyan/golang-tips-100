"""timeit 测量代码执行时间演示"""
import timeit
import time


def list_comprehension():
    return [x * 2 for x in range(100000)]


def list_map():
    return list(map(lambda x: x * 2, range(100000)))


def for_loop():
    result = []
    for x in range(100000):
        result.append(x * 2)
    return result


def demo_timeit_basic():
    """基本用法"""
    t1 = timeit.timeit(list_comprehension, number=1000)
    t2 = timeit.timeit(list_map, number=1000)
    t3 = timeit.timeit(for_loop, number=1000)

    print(f"列表推导式: {t1 / 1000:.6f}s/次")
    print(f"map+lambda: {t2 / 1000:.6f}s/次")
    print(f"for循环:    {t3 / 1000:.6f}s/次")


def demo_repeat():
    """repeat 获取多次结果"""
    results = timeit.repeat(
        list_comprehension,
        number=1000,
        repeat=5,
    )
    print(f"5 次结果: {[f'{r:.4f}s' for r in results]}")
    print(f"最好: {min(results):.4f}s")
    print(f"平均: {sum(results) / len(results):.4f}s")


def demo_string_timeit():
    """直接测量字符串代码"""
    # setup 只执行一次，测量代码执行 number 次
    t = timeit.timeit(
        '"-".join(str(n) for n in range(100))',
        number=10000,
    )
    print(f"join 生成器: {t / 10000:.6f}s/次")

    t = timeit.timeit(
        '"-".join([str(n) for n in range(100)])',
        number=10000,
    )
    print(f"join 列表: {t / 10000:.6f}s/次")


def demo_time_vs_timeit():
    """对比 time.time() 和 timeit"""
    # time.time() 单次测量，受系统影响
    start = time.perf_counter()
    list_comprehension()
    t1 = time.perf_counter() - start
    print(f"time.perf_counter 单次: {t1:.6f}s")

    # timeit 多次测量取平均
    t2 = timeit.timeit(list_comprehension, number=1000) / 1000
    print(f"timeit 1000次平均: {t2:.6f}s")


if __name__ == "__main__":
    print("=== 基本用法 ===")
    demo_timeit_basic()

    print("\n=== repeat 多次测量 ===")
    demo_repeat()

    print("\n=== 字符串代码测量 ===")
    demo_string_timeit()

    print("\n=== time vs timeit ===")
    demo_time_vs_timeit()

    print("\n命令行用法:")
    print('  python -m timeit -s "x = list(range(1000))" "sum(x)"')
    print('  python -m timeit -s "x = list(range(1000))" "[i for i in x if i % 2 == 0]"')
