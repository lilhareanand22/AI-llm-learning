import math
from pathlib import Path


with open("notes.txt", "r") as file:
    content = file.read()
    

print(content)

with open("example.txt", "r") as file:
    lines = file.readline()

print(lines)

with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())
        

#Encoding
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()