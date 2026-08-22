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