"""数据清洗与格式转换常用技巧示例"""
import re
import json
from typing import Any


def clean_text(text: str) -> str:
    """文本清洗：去除多余空白、HTML标签等"""
    # 去除HTML标签
    text = re.sub(r"<[^>]+>", "", text)
    # 去除多个空格/换行
    text = re.sub(r"\s+", " ", text)
    # 去除首尾空白
    return text.strip()


def normalize_keys(data: dict) -> dict:
    """字典key统一为小写下划线"""
    result = {}
    for k, v in data.items():
        # 驼峰转下划线
        new_key = re.sub(r"(?<!^)(?=[A-Z])", "_", k).lower()
        result[new_key] = v
    return result


def safe_int(value: Any, default: int = 0) -> int:
    """安全类型转换"""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def safe_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


def flatten_dict(d: dict, parent_key: str = "", sep: str = ".") -> dict:
    """扁平化嵌套字典"""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def deduplicate_by_field(items: list[dict], field: str) -> list[dict]:
    """按字段去重"""
    seen = set()
    result = []
    for item in items:
        val = item.get(field)
        if val not in seen:
            seen.add(val)
            result.append(item)
    return result


def filter_valid_records(records: list[dict], required_fields: list[str]) -> list[dict]:
    """过滤缺少必需字段的记录"""
    return [r for r in records if all(r.get(f) for f in required_fields)]


def csv_to_jsonl_string(csv_rows: list[dict]) -> str:
    """CSV行数据转JSONL格式字符串"""
    lines = []
    for row in csv_rows:
        lines.append(json.dumps(row, ensure_ascii=False))
    return "\n".join(lines)


def demo_text_cleaning():
    """文本清洗"""
    print("=== 文本清洗 ===")
    dirty = "<p>  Hello   World  </p>\n\n<p>这是  一段  文本。</p>"
    clean = clean_text(dirty)
    print(f"  原始: {dirty!r}")
    print(f"  清洗: {clean!r}")


def demo_key_normalization():
    """Key标准化"""
    print("\n=== Key标准化 ===")
    data = {
        "userName": "Alice",
        "userAge": 25,
        "emailAddress": "alice@example.com",
        "isActive": True,
    }
    normalized = normalize_keys(data)
    print(f"  原始: {data}")
    print(f"  标准化: {normalized}")


def demo_safe_conversion():
    """安全类型转换"""
    print("\n=== 安全类型转换 ===")
    values = ["123", "abc", "45.6", None, "", "789"]
    for v in values:
        result = safe_int(v)
        print(f"  safe_int({v!r}) = {result}")


def demo_flatten():
    """扁平化字典"""
    print("\n=== 扁平化字典 ===")
    nested = {
        "user": {
            "name": "Alice",
            "address": {
                "city": "Beijing",
                "zip": "100000"
            }
        },
        "order": {
            "id": "ORD123",
            "total": 99.9
        }
    }
    flat = flatten_dict(nested)
    print(f"  原始: {nested}")
    print(f"  扁平: {flat}")


def demo_dedup():
    """去重"""
    print("\n=== 按字段去重 ===")
    records = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 1, "name": "Alice Copy"},
        {"id": 3, "name": "Charlie"},
        {"id": 2, "name": "Bob Copy"},
    ]
    unique = deduplicate_by_field(records, "id")
    print(f"  原始: {len(records)} 条")
    print(f"  去重: {len(unique)} 条")
    for r in unique:
        print(f"    {r}")


def demo_filter():
    """过滤"""
    print("\n=== 过滤无效记录 ===")
    records = [
        {"name": "Alice", "email": "a@b.com", "age": 25},
        {"name": "Bob", "email": "", "age": 30},
        {"name": "", "email": "c@d.com", "age": 28},
        {"name": "Charlie", "email": "e@f.com", "age": 0},
    ]
    valid = filter_valid_records(records, ["name", "email"])
    print(f"  原始: {len(records)} 条")
    print(f"  有效: {len(valid)} 条")
    for r in valid:
        print(f"    {r}")


def demo_format_conversion():
    """格式转换"""
    print("\n=== 格式转换 ===")
    csv_rows = [
        {"name": "Alice", "age": "25", "city": "Beijing"},
        {"name": "Bob", "age": "30", "city": "Shanghai"},
    ]
    jsonl_str = csv_to_jsonl_string(csv_rows)
    print("CSV -> JSONL:")
    for line in jsonl_str.split("\n"):
        print(f"  {line}")


if __name__ == "__main__":
    demo_text_cleaning()
    demo_key_normalization()
    demo_safe_conversion()
    demo_flatten()
    demo_dedup()
    demo_filter()
    demo_format_conversion()
