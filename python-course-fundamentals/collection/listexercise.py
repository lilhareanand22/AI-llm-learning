numbers = [10, 20, 30, 40, 50]

print(numbers[1])
print(numbers[-1])
print(len(numbers))


numbers = [10, 20, 30]
numbers.append(40)
numbers.remove(20)

for num in numbers:
    print(num)
    
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [x for x in numbers if x%2 == 0] 
print(even_numbers)  

text = ["Kotlin", "Python", "LLM", "AI"]

result = [word for word in text if len(word) > 3]

print(result) 

documents = [
    "Kotlin is great for Android",
    "Python is popular for AI",
    "LLM applications use Python",
    "Android uses Kotlin"
]
list_of_python = [doc for doc in documents if "Python" in doc]
print(list_of_python)