import math
from pathlib import Path


with open("notes.txt", "r") as file:
    content = file.read()
    

print(content)

with open("example.txt", "r") as file:
    lines = file.readline()

print(lines)