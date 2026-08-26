import csv

employees = [
    ["Anand", 35, "Android Developer"],
    ["Rahul", 30, "Backend Developer"],
    ["Priya", 28, "Data Scientist"]
]

with open("employees.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age", "role"])

    writer.writerows(employees)
    
    
    