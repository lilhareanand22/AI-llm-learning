
import json

user = {
    "name": "Anand",
    "age" : 35
}

json_string = json.dumps(user)
print(json_string)


# converting json string in dictionary 
json_string = '{"name": "Anand", "age": 35}'

user = json.loads(json_string)

print(user)
print(user["name"])

# Nested Jason
data = {
    "user": {
        "name": "Anand",
        "skills": [
            "Kotlin",
            "Android",
            "Python"
        ]
    }
}
print(data["user"]["name"])
print(data["user"]["skills"][0])

# Json Api Resonse
response = '{"id": "123", "model": "some-model", "response": "Python is a programming language."}'

data = json.loads(response)

print(data["model"])

# Json with Exception Handling
response = '{"name": "Anand", "age": 35}'
#response = '{"name": "Anand", "age": }'

try:
    data = json.loads(response)
    print(data["name"])

except json.JSONDecodeError:
    print("Invalid JSON")
    
    
#Json filr write
config = {
    "model": "my-model",
    "temperature": 0.7,
    "max_tokens": 500
}

with open("config.json", "w", encoding="utf-8") as file:
    json.dump(config, file, indent=4)
    
# Json File read
with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

print(config["model"])
print(config["temperature"])
    
    