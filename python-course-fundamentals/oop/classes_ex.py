class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello {self.name}")


user = User("Anand", 35)
print(user.name)
print(user.age)
user.greet()

