import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY is not set. Add it to your .env file or environment variables."
    )

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an eastern poet."},
        {
            "role": "user",
            "content": """Write me a short poem about the moon.
               Write the poem in the style of a haiku.
               Make sure to include a title for the poem.""",
        },
    ],
)

print(response.choices[0].message.content)
