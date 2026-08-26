employees = [
    {"name": "Anand", "age": 35},
    {"name": "Rahul", "age": 30},
    {"name": "Priya", "age": 28}
]

for employee in employees:
    print(employee["name"])
    
experienced = [
    employee
    for employee in employees
    if employee["age"] > 30
]

for emp in experienced:
    print(emp["name"])