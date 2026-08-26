import pandas as pd

data = {
    "name": ["Anand", "Rahul", "Priya"],
    "age": [35, 30, 28],
    "role": [
        "Android",
        "Backend",
        "Data Scientist"
    ]
}

df = pd.DataFrame(data)

print(df)


df = pd.read_csv("employees.csv")

print(df)