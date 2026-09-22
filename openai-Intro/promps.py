from openai import OpenAI 
import os

from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

model = "gpt-4o-mini"
# == few-shot learning
completion = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "You are a translator."},
        {
            "role": "user",
            "content": """ Translate these sentences: 
            'Hello' -> 'Hola', 
            'Goodbye' -> 'Adiós'. 
            '.
             Now translate: 'Thank you'.""",
        },
    ],
)
#print(completion.choices[0].message.content)

# Direct prompt example with openai / Zero-shot prompting
completion = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
    ],
)

print(completion.choices[0].message.content)

