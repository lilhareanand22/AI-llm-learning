person = ("Anand", 35, "India")
print(person[0])
print(person[1])
print(person[2])

#Tuple unpacking
name, age, country = person
print(name)
print(age)
print(country)

# Swapping Variables
a= 10
b= 20
a, b = b,a
print(a)
print(b)


## list vs set vs tuple
numbers_list = [1, 2, 2, 3]
numbers_tuple = (1, 2, 2, 3)
numbers_set = {1, 2, 2, 3}

print(numbers_list)
print(numbers_tuple)
print(numbers_set)