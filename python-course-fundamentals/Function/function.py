def add(a,b):
    return a+b

print(add(10,6))

def add(a,b) -> Int :
    return a + b

print(add("Hello", "World"))

#default paramter
def greet(name, message="Hello"):
    print(message, name)
    
    
greet("Anand")

greet("Anand", "Good Morning")

#Keyword Arguments
def create_user(name, age, city):
    print(name, age, city)

create_user("Anand",35, "Pune")

create_user(age=38, name="Anand", city="Gondia")

# Multiple Return Values
def get_user():
    return"Anand", 35

name, age = get_user()
print(name)
print(age)

# *args
def add_all(*numbers):
   return sum(numbers)

print(add_all(1,2,3,4,5,6,7,8,9,0))

def print_user(**details):
    print(details)
    
print_user(
    name = "Anand",
    age=35,
    city="Pune"
)

# Lambda Functions
square = lambda x: x * x

print(square(5))

numbers = [1,2,3,4,5]
squarelist = list(map(lambda x: x * x, numbers))
print(squarelist)

# Funtions Are First-Class Object
def greet(name):
    return (f"Hello {name}")
    
message_function = greet
print(message_function("Anand"))

# passing parameter as function
def execute(function, value):
    return function(value)

def square(x):
    return x*x

result = execute(square, 5)
print(result)