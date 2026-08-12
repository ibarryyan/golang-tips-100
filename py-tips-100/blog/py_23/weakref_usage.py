"""weakref弱引用使用场景示例"""
import weakref


class Config:
    """配置类，演示弱引用"""
    def __init__(self, env: str):
        self.env = env

    def __repr__(self):
        return f"Config(env={self.env!r})"


class ImageLoader:
    """使用WeakValueDictionary做缓存"""
    _cache = weakref.WeakValueDictionary()

    @classmethod
    def load(cls, path: str) -> dict:
        img = cls._cache.get(path)
        if img is None:
            img = {"path": path, "data": f"image_data_{path}"}
            cls._cache[path] = img
            print(f"  [cache miss] 加载: {path}")
        else:
            print(f"  [cache hit]  命中: {path}")
        return img


def demo_basic_weakref():
    """基础弱引用"""
    print("=== 基础弱引用 ===")
    config = Config("prod")
    weak_config = weakref.ref(config)

    print(f"原对象: {config}")
    print(f"弱引用指向: {weak_config()}")
    print(f"弱引用是否存活: {weak_config() is not None}")

    del config
    print(f"删除原对象后弱引用: {weak_config()}")  # None


def demo_weak_value_dict():
    """WeakValueDictionary缓存"""
    print("\n=== WeakValueDictionary 缓存 ===")

    # 第一次加载，缓存未命中
    img1 = ImageLoader.load("/images/logo.png")
    img2 = ImageLoader.load("/images/logo.png")  # 缓存命中

    print(f"同一对象? {img1 is img2}")  # True

    # 删除外部引用后缓存失效
    del img1, img2
    import gc
    gc.collect()

    img3 = ImageLoader.load("/images/logo.png")  # 再次缓存未命中
    print(f"重新加载: {img3}")


def demo_weak_set():
    """WeakSet演示观察者模式"""
    print("\n=== WeakSet 观察者模式 ===")

    class EventEmitter:
        def __init__(self):
            self._listeners = weakref.WeakSet()

        def add_listener(self, listener):
            self._listeners.add(listener)

        def emit(self, event: str):
            for listener in self._listeners:
                listener(event)

    emitter = EventEmitter()

    class Handler:
        def __call__(self, event: str):
            print(f"  收到事件: {event}")

    h1 = Handler()
    h2 = Handler()
    emitter.add_listener(h1)
    emitter.add_listener(h2)

    emitter.emit("click")

    del h1  # 删除一个监听器
    emitter.emit("hover")  # 只剩h2响应


if __name__ == "__main__":
    demo_basic_weakref()
    demo_weak_value_dict()
    demo_weak_set()
