"""del语句和垃圾回收时机示例"""
import gc


class Resource:
    """演示__del__和资源清理"""
    def __init__(self, name: str):
        self.name = name
        print(f"  [创建] Resource({name})")

    def __del__(self):
        print(f"  [回收] Resource({self.name}) 被销毁")

    def __repr__(self):
        return f"Resource({self.name!r})"


class DBConnection:
    """推荐写法：使用上下文管理器管理资源"""
    def __init__(self, dsn: str):
        self.dsn = dsn
        self._conn = None

    def __enter__(self):
        self._conn = {"dsn": self.dsn, "connected": True}
        print(f"  [连接] {self.dsn}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._conn:
            self._conn["connected"] = False
            print(f"  [断开] {self.dsn}")
        return False

    def query(self, sql: str) -> str:
        return f"result for: {sql}"


def demo_del_behavior():
    """del只删除引用，不直接销毁对象"""
    print("=== del 删除引用 ===")
    r = Resource("db_connection")
    r2 = r

    print(f"删除r...")
    del r  # 不触发__del__，r2还引用着

    print(f"删除r2...")
    del r2  # 引用计数归零，触发__del__


def demo_context_manager():
    """推荐：用上下文管理器替代__del__"""
    print("\n=== 上下文管理器 ===")
    with DBConnection("postgresql://localhost:5432/mydb") as conn:
        result = conn.query("SELECT * FROM users")
        print(f"  查询结果: {result}")

    print("连接已自动关闭")


def demo_gc_timing():
    """GC回收时机"""
    print("\n=== GC回收时机 ===")

    # 创建循环引用
    class Node:
        def __init__(self, name):
            self.name = name
            self.ref = None

        def __del__(self):
            print(f"  [GC回收] Node({self.name})")

    a = Node("A")
    b = Node("B")
    a.ref = b
    b.ref = a  # 循环引用

    del a
    del b
    print("外部引用已删除，但循环引用对象尚未回收")

    print("手动触发gc.collect()...")
    collected = gc.collect()
    print(f"回收了 {collected} 个对象")


if __name__ == "__main__":
    demo_del_behavior()
    demo_context_manager()
    demo_gc_timing()
