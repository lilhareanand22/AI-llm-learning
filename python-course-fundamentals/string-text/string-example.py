text = """
This is line one.
This is line two.
This is line three.
"""
print(text)
print(len(text))

text = "Android"
print(text[0])
print(text[1])
print(text[6])
print("------------")
print(text[-1])
print(text[-2])

print("------------")
#Slicing
text = "Android"

print(text[0:4])
print(text[2:5])
print(text[:4])
print(text[3:])
print("------------")
print(text[::-1])
print("------------")
text = "X" + text[1:]
print(text)

text = "   Hello World   "

print(text.strip())
text = "Android"
if "Android" in text:
    print("Found")
print("------------")    
text = "Android,Kotlin,Python,AI"

items = text.split(",")

print(items)
print("------------") 
#f-strings
name = "Anand"
experience = 12

message = f"{name} has {experience} years of experience."

print(message)

price = 28.5678

print(f"Price: {price:.2f}")
