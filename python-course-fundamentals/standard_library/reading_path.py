from pathlib import Path

path = Path("notes.txt")

print(path.name)
print(path.suffix)
print(path.stem)
print(path.parent)

content = path.read_text(encoding="utf-8")

print(content)

# writing path
path = Path("output1.txt")

path.write_text(
    "Hello Python",
    encoding="utf-8"
)