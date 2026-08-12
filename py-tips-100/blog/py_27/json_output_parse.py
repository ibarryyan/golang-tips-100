"""结构化输出解析（JSON mode）示例"""
import json
import re
from dataclasses import dataclass


@dataclass
class UserInfo:
    """用户信息模型"""
    name: str
    age: int
    skills: list[str]


def extract_json(text: str) -> dict | list | None:
    """从LLM输出中提取JSON"""
    # 方法1：直接解析
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # 方法2：提取代码块中的JSON
    match = re.search(r"```(?:json)?\s*(.*?)\s*```", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass

    # 方法3：找到第一个{或[到最后一个}或]
    start = text.find("{")
    bracket = "{"
    if start == -1:
        start = text.find("[")
        bracket = "["
    if start != -1:
        end_char = "}" if bracket == "{" else "]"
        end = text.rfind(end_char)
        if end > start:
            try:
                return json.loads(text[start:end + 1])
            except json.JSONDecodeError:
                pass

    return None


def parse_with_model(text: str, model_cls):
    """解析LLM输出并转换为dataclass"""
    raw = extract_json(text)
    if raw is None:
        print("  无法提取JSON")
        return None
    try:
        if model_cls == UserInfo:
            return UserInfo(
                name=raw["name"],
                age=raw["age"],
                skills=raw["skills"]
            )
    except KeyError as e:
        print(f"  缺少必需字段: {e}")
    except TypeError as e:
        print(f"  类型错误: {e}")
    return None


def demo_clean_json():
    """干净的JSON输出"""
    print("=== 干净JSON ===")
    llm_output = '{"name": "Alice", "age": 25, "skills": ["Python", "SQL"]}'
    user = parse_with_model(llm_output, UserInfo)
    print(f"  结果: {user}")


def demo_json_in_codeblock():
    """代码块包裹的JSON"""
    print("\n=== 代码块JSON ===")
    llm_output = '''这是用户信息：
```json
{"name": "Bob", "age": 30, "skills": ["Go", "Rust"]}
```
'''
    user = parse_with_model(llm_output, UserInfo)
    print(f"  结果: {user}")


def demo_json_with_surrounding_text():
    """带多余文本的JSON"""
    print("\n=== 带杂质的JSON ===")
    llm_output = '''好的，我来帮你分析。

根据你的描述，用户信息如下：{"name": "Charlie", "age": 28, "skills": ["Java", "Docker"]}

希望对你有帮助！
'''
    user = parse_with_model(llm_output, UserInfo)
    print(f"  结果: {user}")


def demo_invalid_json():
    """无效JSON处理"""
    print("\n=== 无效JSON ===")
    llm_output = "这不是JSON，只是一段普通文本。"
    result = extract_json(llm_output)
    print(f"  结果: {result}")  # None


def demo_missing_fields():
    """缺少字段"""
    print("\n=== 缺少字段 ===")
    llm_output = '{"name": "Dave", "age": 35}'  # 缺少skills
    user = parse_with_model(llm_output, UserInfo)
    print(f"  结果: {user}")


if __name__ == "__main__":
    demo_clean_json()
    demo_json_in_codeblock()
    demo_json_with_surrounding_text()
    demo_invalid_json()
    demo_missing_fields()
