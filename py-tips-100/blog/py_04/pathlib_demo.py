from pathlib import Path

base_dir = Path("data")
file_path = base_dir / "input.txt"

file_path.parent.mkdir(parents=True, exist_ok=True)
file_path.write_text("hello", encoding="utf-8")

if file_path.exists():
    print(file_path.read_text(encoding="utf-8"))

file_path.unlink()
file_path.parent.rmdir()
