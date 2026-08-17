
name : str ="anand"
age :int = 38
salary = 28.5
active = True
print(f"My name is {name.upper()} and age is {age}")
is_android_developer : bool = True
middle_name : str | None = f"My name is {name.upper()} and age is {age}"

if middle_name is not None:
    print(len(middle_name))
    
print(type(name))
print(type(age))
print(type(salary))
print(type(active))
    