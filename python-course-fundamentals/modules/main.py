import math_utils
from lambda_ex import maximum
import squre_ex as squarelist
from utils.calculator import add

print(math_utils.add(10,20))
print(math_utils.multipley(10,5))

numbers = [1,4,3,2,7,6,8,3]
print(maximum(numbers))


result = squarelist.square(lambda x : x * x, numbers)
print(result)

print(add(10, 30))


