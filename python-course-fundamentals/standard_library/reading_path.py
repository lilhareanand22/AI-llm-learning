from pathlib import Path

path = Path("notes.txt")

content = path.read_text(encoding="utf-8")

print(content)

# writing path
path = Path("output1.txt")

path.write_text(
    "Hello Python",
    encoding="utf-8"
)