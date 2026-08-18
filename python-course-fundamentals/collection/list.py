numbers = [10,20,30,40]
print(numbers[0])
print(numbers[1])
print(len(numbers))
numbers.append(50)
print(numbers)
numbers.remove(10)
print(numbers)

# check whether a number is present in the list or not
if 20 in numbers:
    print("Found")
    
# Loop through list
for  num in numbers:
    print(num)
    
# index + value - enumerate()
for i, number in enumerate(numbers):
    print(f"{i}: {number}")
    
# Slicing 
numbers = [10, 20, 30, 40, 50]
print("--------------")
print(numbers[0:3])
print(numbers[2:])
print(numbers[-2:])

# map equivalent to list
print("--------------")
numbers = [1, 2, 3, 4]

result = [x * 2 for x in numbers]
print(result)

# filter equivalent
print("--------------")
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)