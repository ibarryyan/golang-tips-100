"""大文件分块读取与处理示例"""
import json
import csv
import os
import tempfile
from typing import Iterator
from pathlib import Path


def read_jsonl(path: str) -> Iterator[dict]:
    """逐行读取JSONL文件"""
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)


def write_jsonl(path: str, records: list[dict]):
    """写入JSONL文件"""
    with open(path, "w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


def process_large_csv(path: str, batch_size: int = 1000) -> Iterator[list[dict]]:
    """分批读取CSV"""
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        batch = []
        for row in reader:
            batch.append(row)
            if len(batch) >= batch_size:
                yield batch
                batch = []
        if batch:
            yield batch


def demo_jsonl():
    """JSONL处理演示"""
    print("=== JSONL文件处理 ===")
    tmpdir = tempfile.mkdtemp()
    jsonl_path = os.path.join(tmpdir, "data.jsonl")

    # 写入测试数据
    records = [
        {"id": 1, "text": "第一条记录", "label": "positive"},
        {"id": 2, "text": "第二条记录", "label": "negative"},
        {"id": 3, "text": "第三条记录", "label": "neutral"},
    ]
    write_jsonl(jsonl_path, records)
    print(f"  写入 {len(records)} 条记录到 {jsonl_path}")

    # 逐行读取
    count = 0
    for record in read_jsonl(jsonl_path):
        print(f"  读取: {record}")
        count += 1
    print(f"  共读取 {count} 条")

    # 清理
    os.remove(jsonl_path)
    os.rmdir(tmpdir)


def demo_csv_batch():
    """CSV分批处理演示"""
    print("\n=== CSV分批处理 ===")
    tmpdir = tempfile.mkdtemp()
    csv_path = os.path.join(tmpdir, "data.csv")

    # 写入测试数据
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "score"])
        for i in range(25):
            writer.writerow([i, f"user_{i}", 80 + i % 20])

    # 分批读取
    total = 0
    for i, batch in enumerate(process_large_csv(csv_path, batch_size=10)):
        print(f"  批次{i}: {len(batch)}行, 首行: {batch[0]}")
        total += len(batch)
    print(f"  共读取 {total} 行")

    # 清理
    os.remove(csv_path)
    os.rmdir(tmpdir)


def demo_file_size_estimate():
    """估算文件大小"""
    print("\n=== 文件信息 ===")
    tmpdir = tempfile.mkdtemp()
    file_path = os.path.join(tmpdir, "test.txt")

    content = "Hello, " * 1000
    with open(file_path, "w") as f:
        f.write(content)

    size = os.path.getsize(file_path)
    print(f"  文件大小: {size} bytes ({size / 1024:.1f} KB)")

    # 流式读取
    chunk_size = 1024
    with open(file_path, "r") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            print(f"  读取块: {len(chunk)} 字符")

    os.remove(file_path)
    os.rmdir(tmpdir)


def demo_line_by_line():
    """逐行处理大文本"""
    print("\n=== 逐行处理 ===")
    tmpdir = tempfile.mkdtemp()
    file_path = os.path.join(tmpdir, "big.txt")

    # 模拟大文件
    with open(file_path, "w") as f:
        for i in range(100):
            f.write(f"Line {i}: This is a sample line of text.\n")

    # 逐行处理，内存占用恒定
    line_count = 0
    total_length = 0
    with open(file_path, "r") as f:
        for line in f:
            line_count += 1
            total_length += len(line)

    print(f"  总行数: {line_count}")
    print(f"  总字符: {total_length}")

    os.remove(file_path)
    os.rmdir(tmpdir)


if __name__ == "__main__":
    demo_jsonl()
    demo_csv_batch()
    demo_file_size_estimate()
    demo_line_by_line()
