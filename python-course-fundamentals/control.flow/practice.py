for i in range(20):
    if i%2 == 0:
        print(i)
        
        
for i in range(10,0,-1):
    print(i)

numbers = [10, 20, 30, 40, 50]

sum = 0
for i in numbers:
    sum += i
    
print(sum)

target = 30
for i in numbers:
    if(i == target):
        print("Found")
        break
else :
    print("Not Found")    
    
    
if target in numbers:
    print("Found")
    
names = ["Anand", "Rahul", "Amit", "Raj"]
for (key, value) in enumerate(names):
    print(key, value)
 