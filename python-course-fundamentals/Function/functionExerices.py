
def calculate_area(lenght,width):
    return lenght * width

print(calculate_area(10,5))


def greet(name, message="Hello"):
    print(message, name)

greet("Anand")
greet("Anand", "Good Morning")

def get_mini_max(numbers):
    return min(numbers), max(numbers)

numbers = [10, 5, 20,3,15]
minimum, maxmimum = get_mini_max(numbers)
print(minimum)
print(maxmimum)

def calculate_sum(*numbers):
    return sum(numbers)

print(calculate_sum(10,20))
print(calculate_sum(10,20,30,40))

def print_profile(**profile):
    print(profile)
    
print_profile(
    name="Anand",
    role="Android Developer",
    experience=12
)

cube = lambda x: x*x*x
print(cube(3))

def process_number(number, operation):
    return list(map(operation, number))

numbers = [1,2,3,4,5]
result = process_number(
    numbers,
    lambda x: x * x
)

print(result)