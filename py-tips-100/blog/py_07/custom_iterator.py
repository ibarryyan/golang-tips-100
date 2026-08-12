"""自定义迭代器实现__iter__和__next__"""


class CountDown:
    """倒计时迭代器：从 n 倒数到 1"""

    def __init__(self, start):
        self.current = start

    # __iter__ 返回迭代器对象本身
    def __iter__(self):
        self.current = self._start  # 重置以便可重复迭代
        return self

    # __next__ 返回下一个值，没有更多值时抛出 StopIteration
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

    # 初始化原始起始值
    def __post_init__(self):
        pass

    _start = 0


# 正确写法：保存起始值
class CountDownFixed:
    """可重复迭代的倒计时器"""

    def __init__(self, start):
        self._start = start
        self._current = start

    def __iter__(self):
        # 每次迭代前重置游标
        self._current = self._start
        return self

    def __next__(self):
        if self._current <= 0:
            raise StopIteration
        self._current -= 1
        return self._current + 1


# 使用
cd = CountDownFixed(5)
for num in cd:
    print(num, end=" ")  # 5 4 3 2 1
print()

# 可以重复迭代（因为 __iter__ 会重置）
for num in cd:
    print(num, end=" ")  # 5 4 3 2 1
print()

# 也可以手动 next
cd2 = CountDownFixed(3)
it = iter(cd2)  # 调用 __iter__
print(next(it))  # 3
print(next(it))  # 2
print(next(it))  # 1
# print(next(it))  # StopIteration


# === 更实用的例子：分页迭代器 ===
class PageIterator:
    """模拟分页遍历大数据"""

    def __init__(self, total, page_size):
        self._total = total
        self._page_size = page_size

    def __iter__(self):
        self._offset = 0
        return self

    def __next__(self):
        if self._offset >= self._total:
            raise StopIteration
        end = min(self._offset + self._page_size, self._total)
        page = list(range(self._offset, end))
        self._offset = end
        return page


pages = PageIterator(10, 3)
for page in pages:
    print(f"页数据: {page}")
# 页数据: [0, 1, 2]
# 页数据: [3, 4, 5]
# 页数据: [6, 7, 8]
# 页数据: [9]
