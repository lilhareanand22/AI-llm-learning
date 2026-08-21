# Loop Through a List
numbers = [10,20,30]
for number in numbers:
    print(number)
  
# Loop Through a Set
numbers = {10, 20, 30}

for number in numbers:
    print(number)
    
    
# Loops Through a dictionary
person = {
    "name": "Anand",
    "age": 35,
    "role": "Android Developer"
}

for key in person:
    print(key)
    
for value in person.values():
    print(value)

for key, value in person.items():
    print(key, value)
    
    
# for loop with range
for i in range(5):
    print(i)  

for i in range(2,10,2):
    print(i) 

# Reverse Loop
for i in range(10,0, -2):
    print(i) 

# break conept
for i in range(10):
    if i== 5:
        break
    
    print(i)
    
# continue
for i in range(5):
    if i == 2:
        continue
    print(i)

#pass
for i in range(5):
    if i == 2:
        pass
    else:
        print(i)   
        
#enumerate()
names = ["Anand", "Rahul", "Amit"]
for index, name in enumerate(names):
    print(index, name)