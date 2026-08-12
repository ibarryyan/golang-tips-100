"""引用计数与gc模块示例"""
import sys
import gc


class Node:
    """演示循环引用的节点类"""
    def __init__(self, name: str):
        self.name = name
        self.parent = None
        self.children = []

    def __repr__(self):
        return f"Node({self.name!r})"


def demo_ref_count():
    """引用计数基础"""
    a = [1, 2, 3]
    print(f"初始引用计数: {sys.getrefcount(a)}")  # 2（变量a + 函数参数）

    b = a
    print(f"赋值给b后: {sys.getrefcount(a)}")  # 3

    c = a
    print(f"赋值给c后: {sys.getrefcount(a)}")  # 4

    del b
    print(f"删除b后: {sys.getrefcount(a)}")  # 3

    del c
    print(f"删除c后: {sys.getrefcount(a)}")  # 2


def demo_circular_ref():
    """循环引用问题"""
    root = Node("root")
    child = Node("child")

    root.children.append(child)
    child.parent = root  # 形成循环引用

    print(f"\n循环引用创建完成: {root} -> {child} -> {root}")

    # 删除外部引用
    del root
    del child

    # 手动触发GC检测循环引用
    collected = gc.collect()
    print(f"GC回收的对象数: {collected}")


def demo_gc_info():
    """gc模块信息"""
    print(f"\nGC统计信息: {gc.get_count()}")
    print(f"GC阈值: {gc.get_threshold()}")
    print(f"GC是否开启: {gc.isenabled()}")

    # 获取所有追踪的对象
    all_objects = gc.get_objects()
    print(f"当前被GC追踪的对象总数: {len(all_objects)}")


if __name__ == "__main__":
    demo_ref_count()
    demo_circular_ref()
    demo_gc_info()
