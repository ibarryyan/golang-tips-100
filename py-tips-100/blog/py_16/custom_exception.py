"""自定义异常类"""


# === 异常继承体系 ===
class AppError(Exception):
    """应用所有异常的基类"""
    pass


class DatabaseError(AppError):
    """数据库相关异常"""
    pass


class NetworkError(AppError):
    """网络相关异常"""
    pass


class ConfigError(AppError):
    """配置相关异常"""
    pass


# === 业务异常 ===
class DivisionError(Exception):
    """除法相关异常基类"""
    pass


class ZeroDivError(DivisionError):
    """除数为零"""
    pass


class NegativeNumberError(DivisionError):
    """负数错误"""
    pass


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivError("除数不能为零")
    if a < 0 or b < 0:
        raise NegativeNumberError("不支持负数运算")
    return a / b


# 按异常类型分别处理
for a, b in [(10, 2), (10, 0), (-5, 2)]:
    try:
        result = divide(a, b)
        print(f"{a} / {b} = {result}")
    except ZeroDivError as e:
        print(f"{a} / {b} -> 除零错误: {e}")
    except NegativeNumberError as e:
        print(f"{a} / {b} -> 负数错误: {e}")


# === 携带额外信息的异常 ===
class ValidationError(Exception):
    def __init__(self, field: str, value, message: str = ""):
        self.field = field
        self.value = value
        self.message = message or f"字段 '{field}' 的值 '{value}' 无效"
        super().__init__(self.message)


def validate_age(age: int) -> None:
    if age < 0:
        raise ValidationError("age", age, "年龄不能为负数")
    if age > 150:
        raise ValidationError("age", age, "年龄不合法")


for age in [18, -5, 200]:
    try:
        validate_age(age)
        print(f"年龄 {age} 验证通过")
    except ValidationError as e:
        print(f"年龄 {age} 验证失败: 字段={e.field}, 值={e.value}, 信息={e.message}")
