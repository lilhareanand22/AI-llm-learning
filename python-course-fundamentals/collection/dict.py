user = {
    "name": "Anand",
    "age": 35,
    "role": "Android Developer"
}
print(user["name"])


if "name" in user:
    print("Name exists")
    
print(user.get("name"))
print(user.get("role"))

city = user["age"]
print(city)

key = user.keys()
print(key)
keys = list(user.keys())
print(keys)
print(user.values())

for  key, value in user.items():
    print(f"{key}:{value}")
    
#Nested Dictionary
user = {
    "name" : "Anand",
    "skills": {
        "android":["kotlin", "compose", "Coroutines"],
        "ai": ["python", "LLM", "ML"]
    }
}
print(user["name"])
print(user["skills"]["android"])
print(user["skills"]["android"][0])

# Dictionary + List Together
documents = [
    {
        "id": 1,
        "text": "Kotlin is used for Android",
        "metadata": {
            "language": "Kotlin",
            "topic": "Android"
        }
    },
    {
        "id": 2,
        "text": "Python is used for AI",
        "metadata": {
            "language": "Python",
            "topic": "AI"
        }
    }
]
texts = [doc["metadata"]["language"] for doc in documents]
print(texts)

numbers = [1, 2, 3, 4]

result = {
    x: x * 2
    for x in numbers
}

print(result)