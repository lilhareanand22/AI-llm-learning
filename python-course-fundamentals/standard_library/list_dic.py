from pathlib import Path

folder = Path("data")

for item in folder.iterdir():
    print(item)
    

# Find Only txt file    
for file in folder.glob("*.txt"):
    print(file)
    
    
#Recursive search

for file in folder.rglob("*.txt"):
    print(file)