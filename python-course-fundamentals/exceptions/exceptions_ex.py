

try:
    number = int("hello")
except ValueError:
    print("Invalid number")
    
    
# Catch the Exception Object
try:
    numbers: int("Hello")
except ValueError as e:
    print(e) 
    
    
#Multiple Exception

try:
    num = int(input("Enter number:"))
    result = 100 / num
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
    
# Catch multiple exception

try:
    num = int(input("Enter number:"))
    result = 100 / num
except (ValueError, TypeError):
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
    
    
# else in expection

try:
    number = int("100")
except ValueError:
    print("Invalid number")
else:
    print("Conversion successful") 
    
# Finally
try:
    number = int("100")
except ValueError:
    print("Invalid")
finally:
    print("Finished") 
    
# raise

def set_age(age):
    if age < 1 :
        raise ValueError("Age can not be negative")
    return age

result = set_age(10)
print(result)

#set_age(0)

# Custom Exception
class InvalidAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise InvalidAgeError("Invalid age")

    return age
