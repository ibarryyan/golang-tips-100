"""Prompt模板管理与复用示例"""
from string import Template
from dataclasses import dataclass
from typing import Any


@dataclass
class Message:
    """消息结构"""
    role: str  # system / user / assistant
    content: str

    def __repr__(self):
        return f"[{self.role}] {self.content[:50]}..."


class PromptTemplate:
    """Prompt模板"""

    def __init__(self, template: str):
        self.template = Template(template)

    def render(self, **kwargs) -> str:
        return self.template.safe_substitute(**kwargs)


class PromptManager:
    """Prompt模板注册与管理"""
    _templates: dict[str, PromptTemplate] = {}

    @classmethod
    def register(cls, name: str, template: str):
        cls._templates[name] = PromptTemplate(template)

    @classmethod
    def build(cls, name: str, **vars) -> list[Message]:
        tpl = cls._templates.get(name)
        if tpl is None:
            raise KeyError(f"Prompt模板 '{name}' 未注册")
        rendered = tpl.render(**vars)
        return [Message(role="user", content=rendered)]

    @classmethod
    def build_with_system(cls, name: str, system_prompt: str, **vars) -> list[Message]:
        messages = [Message(role="system", content=system_prompt)]
        messages.extend(cls.build(name, **vars))
        return messages


def demo_basic_template():
    """基础模板"""
    print("=== 基础模板 ===")
    template = PromptTemplate(
        "你是一个$role。\n"
        "请遵循以下规则：\n"
        "1. 用中文回答\n"
        "2. 回答简洁，不超过$max_words字\n"
        "3. 如果不确定，请说'我不确定'\n"
    )
    rendered = template.render(role="技术顾问", max_words="200")
    print(rendered)


def demo_prompt_manager():
    """Prompt管理器"""
    print("\n=== Prompt管理器 ===")
    # 注册模板
    PromptManager.register("summarize", "请总结以下文本：\n\n$text")
    PromptManager.register("translate", "请将以下文本翻译为$language：\n\n$text")
    PromptManager.register(
        "code_review",
        "请审查以下代码，关注$focus方面：\n\n```\n$code\n```"
    )

    # 使用
    messages = PromptManager.build("translate", text="Hello World", language="中文")
    print(f"  translate: {messages}")

    messages = PromptManager.build("summarize", text="Python是一门优秀的...")
    print(f"  summarize: {messages}")

    messages = PromptManager.build(
        "code_review",
        focus="性能和安全",
        code="def add(a, b): return a + b"
    )
    print(f"  code_review: {messages}")


def demo_system_prompt():
    """带系统提示词"""
    print("\n=== 带系统提示词 ===")
    PromptManager.register("ask", "问题：$question")

    messages = PromptManager.build_with_system(
        "ask",
        system_prompt="你是一个专业的Python开发者，回答技术问题。",
        question="如何处理Python中的循环引用？"
    )
    for msg in messages:
        print(f"  {msg}")


def demo_few_shot():
    """Few-shot模板"""
    print("\n=== Few-shot模板 ===")
    few_shot = PromptTemplate(
        "任务：对用户评论进行情感分析。\n\n"
        "示例：\n"
        "输入：这个产品太棒了！\n输出：正面\n"
        "输入：质量很差，不推荐。\n输出：负面\n\n"
        "现在请分析：\n输入：$input\n输出："
    )
    prompt = few_shot.render(input="价格合理，性能不错，但包装一般。")
    print(f"  {prompt}")


if __name__ == "__main__":
    demo_basic_template()
    demo_prompt_manager()
    demo_system_prompt()
    demo_few_shot()
