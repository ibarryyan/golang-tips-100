from pathlib import Path

file_path = Path("demo.txt")

with file_path.open("w", encoding="utf-8") as file:
    file.write("hello")

with file_path.open("r", encoding="utf-8") as file:
    content = file.read()

print(content)

file_path.unlink()
