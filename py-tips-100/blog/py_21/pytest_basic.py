"""pytest 基础用法演示"""


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b


# === 基础测试 ===
def test_add():
    assert add(1, 2) == 3


def test_add_negative():
    assert add(-1, -2) == -3


def test_add_zero():
    assert add(0, 0) == 0
    assert add(5, 0) == 5


# === 异常测试 ===
def test_divide():
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    import pytest
    with pytest.raises(ValueError, match="除数不能为零"):
        divide(10, 0)


# === 测试多个断言 ===
def test_add_properties():
    # 交换律
    assert add(3, 5) == add(5, 3)
    # 结合律
    assert add(add(1, 2), 3) == add(1, add(2, 3))
    # 零元
    assert add(x := 42, 0) == x


if __name__ == "__main__":
    # 直接运行查看结果（实际用 pytest 运行）
    test_add()
    test_add_negative()
    test_add_zero()
    test_divide()
    test_divide_by_zero()
    test_add_properties()
    print("所有测试通过！")
    print("\n运行 pytest: pytest pytest_basic.py -v")
