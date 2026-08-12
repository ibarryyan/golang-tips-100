"""流式响应处理与SSE示例"""
import json
import time
from typing import Generator


class StreamProcessor:
    """流式响应处理器"""

    @staticmethod
    def parse_sse_line(line: str) -> dict | None:
        """解析SSE单行"""
        line = line.strip()
        if not line:
            return None
        if not line.startswith("data: "):
            return None
        data = line[6:].strip()
        if data == "[DONE]":
            return {"done": True}
        try:
            return json.loads(data)
        except json.JSONDecodeError:
            return None

    @staticmethod
    def consume_stream(lines: Generator[str, None, None]) -> str:
        """消费流并返回完整文本"""
        full_text = ""
        for line in lines:
            data = StreamProcessor.parse_sse_line(line)
            if data is None:
                continue
            if data.get("done"):
                break
            if "content" in data:
                full_text += data["content"]
                print(data["content"], end="", flush=True)
        print()  # 换行
        return full_text


def simulate_llm_stream() -> Generator[str, None, None]:
    """模拟LLM流式返回（SSE格式）"""
    chunks = ["你好", "，我是", "AI助手", "。", "有什么", "可以", "帮你？"]
    for chunk in chunks:
        yield f"data: {json.dumps({'content': chunk})}\n\n"
        time.sleep(0.1)
    yield "data: [DONE]\n\n"


def simulate_error_stream() -> Generator[str, None, None]:
    """模拟带错误信息的流"""
    yield f"data: {json.dumps({'content': '正在'})}\n\n"
    yield f"data: {json.dumps({'content': '处理...'})}\n\n"
    yield f"data: {json.dumps({'error': 'rate_limit_exceeded'})}\n\n"
    yield "data: [DONE]\n\n"


def demo_basic_stream():
    """基础流式处理"""
    print("=== 基础流式处理 ===")
    full = StreamProcessor.consume_stream(simulate_llm_stream())
    print(f"  完整响应: {full}")


def demo_error_handling():
    """错误处理"""
    print("\n=== 错误处理 ===")
    full_text = ""
    for line in simulate_error_stream():
        data = StreamProcessor.parse_sse_line(line)
        if data is None:
            continue
        if data.get("done"):
            break
        if "error" in data:
            print(f"\n  [错误] {data['error']}")
            break
        if "content" in data:
            full_text += data["content"]
            print(data["content"], end="", flush=True)
    print()


def demo_callback_pattern():
    """回调模式处理流"""
    print("\n=== 回调模式 ===")

    def on_chunk(chunk: str):
        print(f"[chunk] {chunk}", end="")

    def on_complete(full: str):
        print(f"\n[complete] 共{len(full)}字符")

    def on_error(err: str):
        print(f"\n[error] {err}")

    def process(lines: Generator[str, None, None]):
        full = ""
        for line in lines:
            data = StreamProcessor.parse_sse_line(line)
            if data is None:
                continue
            if data.get("done"):
                on_complete(full)
                return full
            if "error" in data:
                on_error(data["error"])
                return full
            if "content" in data:
                full += data["content"]
                on_chunk(data["content"])
        return full

    process(simulate_llm_stream())


def demo_sse_format():
    """SSE格式说明"""
    print("\n=== SSE格式 ===")
    sample = (
        "data: {\"content\": \"Hello\"}\n"
        "\n"
        "data: {\"content\": \" World\"}\n"
        "\n"
        "data: [DONE]\n"
        "\n"
    )
    print(f"SSE原始格式示例:\n{sample}")
    print("解析结果:")
    for line in sample.split("\n"):
        data = StreamProcessor.parse_sse_line(line)
        if data:
            print(f"  {data}")


if __name__ == "__main__":
    demo_basic_stream()
    demo_error_handling()
    demo_callback_pattern()
    demo_sse_format()
