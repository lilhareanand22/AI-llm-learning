numbers:set = {1,1,2,3,5,4,6}
print(numbers)

numbers.add(7)
numbers.remove(1)
print(numbers)

numbers2 = set()
print(numbers2)

#Union
a = {1,2,3,4,5}
b = {4,5,6,7,8,}
print(a | b)
print(a.union(b))

#Intersection
print(a & b)
print(a.intersection(b))

##Difference
print(b-a)
print(a.difference(b))

##Symmetic Difference
print(a ^ b)
print(a.symmetric_difference(b))

#Membership Check
if 5 in a:
    print("Found")