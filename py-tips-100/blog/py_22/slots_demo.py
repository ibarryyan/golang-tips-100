"""__slots__ 减少内存占用演示"""
import sys


class PointDict:
    """普通类，使用 __dict__ 存储属性"""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class PointSlots:
    """使用 __slots__，固定属性列表"""
    __slots__ = ("x", "y", "z")

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def demo_memory_comparison():
    """对比内存占用"""
    p1 = PointDict(1, 2, 3)
    p2 = PointSlots(1, 2, 3)

    print(f"普通类对象: {sys.getsizeof(p1)} 字节")
    print(f"  + __dict__: {sys.getsizeof(p1.__dict__)} 字节")
    print(f"  总计: {sys.getsizeof(p1) + sys.getsizeof(p1.__dict__)} 字节")

    print(f"slots类对象: {sys.getsizeof(p2)} 字节")
    try:
        p2.__dict__
    except AttributeError:
        print(f"  无 __dict__")
    print(f"  总计: {sys.getsizeof(p2)} 字节")

    saving = (sys.getsizeof(p1) + sys.getsizeof(p1.__dict__) - sys.getsizeof(p2))
    saving_pct = saving / (sys.getsizeof(p1) + sys.getsizeof(p1.__dict__)) * 100
    print(f"  节省: {saving} 字节 ({saving_pct:.0f}%)")


def demo_bulk_memory():
    """大量对象的内存对比"""
    N = 100000

    points_dict = [PointDict(1, 2, 3) for _ in range(N)]
    points_slots = [PointSlots(1, 2, 3) for _ in range(N)]

    # 使用 tracemalloc 测量实际分配内存
    import tracemalloc

    tracemalloc.start()
    _ = [PointDict(1, 2, 3) for _ in range(N)]
    current_dict, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    tracemalloc.start()
    _ = [PointSlots(1, 2, 3) for _ in range(N)]
    current_slots, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"\n{N} 个对象内存分配:")
    print(f"  普通类: {current_dict / 1024 / 1024:.1f} MB")
    print(f"  slots类: {current_slots / 1024 / 1024:.1f} MB")
    print(f"  节省: {(current_dict - current_slots) / 1024 / 1024:.1f} MB")

    # 保持引用防止 GC
    _ = points_dict
    _ = points_slots


def demo_attribute_access():
    """属性访问速度对比"""
    import timeit

    p1 = PointDict(1, 2, 3)
    p2 = PointSlots(1, 2, 3)

    t1 = timeit.timeit(lambda: p1.x, number=10_000_000)
    t2 = timeit.timeit(lambda: p2.x, number=10_000_000)

    print(f"\n属性访问 (1000万次):")
    print(f"  普通类: {t1:.3f}s")
    print(f"  slots类: {t2:.3f}s")


def demo_dynamic_attribute():
    """__slots__ 禁止动态添加属性"""
    p = PointSlots(1, 2, 3)

    try:
        p.new_attr = 42
    except AttributeError as e:
        print(f"\n动态添加属性失败: {e}")
        print("__slots__ 只允许声明的属性: ('x', 'y', 'z')")


if __name__ == "__main__":
    print("=== 内存对比 ===")
    demo_memory_comparison()

    print("\n=== 大量对象内存 ===")
    demo_bulk_memory()

    print("\n=== 属性访问速度 ===")
    demo_attribute_access()

    print("\n=== 动态属性限制 ===")
    demo_dynamic_attribute()

    print("\n使用建议:")
    print("  - 大量同类对象时使用 __slots__")
    print("  - 不需要动态添加属性时使用")
    print("  - 继承时子类也需声明 __slots__")
    print("  - 与 dataclass 配合使用效果更好")
