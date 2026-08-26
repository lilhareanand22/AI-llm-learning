import requests
from dotenv import load_dotenv
import os

#response = requests.get("https://example.com")

#print(response.status_code)


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print(api_key)