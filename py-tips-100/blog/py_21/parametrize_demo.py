"""pytest parametrize 参数化测试演示"""
import pytest


def add(a, b):
    return a + b


def is_palindrome(s):
    return s == s[::-1]


def classify_number(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"


# === 基本参数化 ===
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_add(a, b, expected):
    assert add(a, b) == expected


# === 带 ID 的参数化 ===
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("hello", "HELLO"),
        ("World", "WORLD"),
        ("", ""),
        ("123abc", "123ABC"),
    ],
    ids=["lowercase", "mixed", "empty", "alphanumeric"],
)
def test_upper(input_str, expected):
    assert input_str.upper() == expected


# === 参数化异常测试 ===
def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b


@pytest.mark.parametrize("a, b", [
    (10, 0),
    (0, 0),
    (-5, 0),
])
def test_divide_by_zero(a, b):
    with pytest.raises(ValueError, match="除数不能为零"):
        divide(a, b)


# === 笛卡尔积参数化 ===
@pytest.mark.parametrize("x", [1, 2, 3])
@pytest.mark.parametrize("y", [10, 20])
def test_multiply_positive(x, y):
    """3×2=6 组测试"""
    assert x * y > 0


# === 多字段参数化 ===
@pytest.mark.parametrize("number, expected", [
    (1, "positive"),
    (42, "positive"),
    (-1, "negative"),
    (-99, "negative"),
    (0, "zero"),
])
def test_classify_number(number, expected):
    assert classify_number(number) == expected


if __name__ == "__main__":
    import subprocess
    result = subprocess.run(
        ["python", "-m", "pytest", __file__, "-v"],
        capture_output=True, text=True,
    )
    print(result.stdout)
