"""any()和all()的短路求值示例"""


def basic_any_all():
    """基础用法"""
    numbers = [0, 0, 3, 0]

    # any遇到第一个True就停止
    result_any = any(n > 0 for n in numbers)
    print(f"  any(n > 0): {result_any}")  # True

    # all遇到第一个False就停止
    result_all = all(n > 0 for n in numbers)
    print(f"  all(n > 0): {result_all}")  # False


def short_circuit_demo():
    """演示短路求值"""
    side_effects = []

    def check(n):
        side_effects.append(n)
        return n > 0

    # any短路：遇到第一个True就停
    side_effects.clear()
    result = any(check(n) for n in [0, 0, 3, 5])
    print(f"  any短路: 结果={result}, 检查了={side_effects}")  # 只检查了[0, 0, 3]

    # all短路：遇到第一个False就停
    side_effects.clear()
    result = all(check(n) for n in [3, 5, 0, 7])
    print(f"  all短路: 结果={result}, 检查了={side_effects}")  # 只检查了[3, 5, 0]


def check_users():
    """实用场景：用户验证"""
    users = [
        {"name": "Alice", "active": True},
        {"name": "Bob", "active": True},
        {"name": "Charlie", "active": False},
    ]

    # 是否有非活跃用户
    has_inactive = any(not u["active"] for u in users)
    print(f"  有非活跃用户: {has_inactive}")  # True

    # 是否所有用户都活跃
    all_active = all(u["active"] for u in users)
    print(f"  所有用户活跃: {all_active}")  # False


def validate_form():
    """实用场景：表单验证"""
    required_fields = ["name", "email", "phone"]
    form_data = {"name": "Tom", "email": "tom@example.com", "phone": ""}

    all_filled = all(form_data.get(f) for f in required_fields)
    print(f"  所有字段已填: {all_filled}")  # False（phone为空）

    has_any_filled = any(form_data.get(f) for f in required_fields)
    print(f"  至少一个字段已填: {has_any_filled}")  # True


def find_in_large_data():
    """大序列中的短路优势"""
    # 模拟一个生成器，避免创建大列表
    def large_range(n):
        for i in range(n):
            print(f"    检查 {i}...")
            yield i

    # any在第5次就停了，不需要遍历100万次
    result = any(x > 3 for x in large_range(1_000_000))
    print(f"  any在100万数据中找>3: {result}")


if __name__ == "__main__":
    print("=== 基础用法 ===")
    basic_any_all()
    print("\n=== 短路求值演示 ===")
    short_circuit_demo()
    print("\n=== 用户验证 ===")
    check_users()
    print("\n=== 表单验证 ===")
    validate_form()
    print("\n=== 大数据短路 ===")
    find_in_large_data()
