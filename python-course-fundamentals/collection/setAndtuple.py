numbers = [1, 2, 2, 3, 4, 4, 5]
numbers_set = set(numbers)
print(numbers_set)


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b)

person = ("Anand", 35, "Android")
name, age, profession = person
print(name)
print(age)
print(profession)

a = 100
b = 200
a,b = b,a
print(a)
print(b)
