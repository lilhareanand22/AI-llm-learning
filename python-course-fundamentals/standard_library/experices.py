from pathlib import Path

path = Path("documents")

path.exists()
path.is_file()
path.is_dir()

path.read_text(encoding="utf-8")
path.write_text("Hello", encoding="utf-8")

path.iterdir()

path.glob("*.txt")
path.rglob("*.txt")

path.name
path.stem
path.suffix
path.parent