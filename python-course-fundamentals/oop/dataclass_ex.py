from dataclasses import dataclass


@dataclass
class User:
    name:str
    age:int
    
user = User("Anand", 37)

print(user)