from pathlib import Path

path = Path("notes.txt")
print(path)

#Check if file exists
if path.exists():
    print("File exists")
else:
    print("File does not exist")
    
#Is it a File?
if path.is_file():
    print("It is a file")
    
#Is it a director?
path = Path("oop")

if path.is_dir():
    print("It is a directory")
else:
   path.mkdir(exist_ok=True) 
   
# create nexted dictory
path1 = Path("data/documents/pdfs")

path1.mkdir(parents=True, exist_ok=True)  


base = Path("data")

file_path = base / "documents" / "file.txt"

print(file_path)