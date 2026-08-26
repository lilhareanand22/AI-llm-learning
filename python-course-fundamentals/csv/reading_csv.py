import csv

with open("employees.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
        

with open("employees.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        #print(row)
        print(row["name"])
    
    
employees = []

with open("employees.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        employees.append(row)
        
print(employees)