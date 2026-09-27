import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
    http_options=types.HttpOptions(timeout=60000)
)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="what is artifical intelligent.",
    config=types.GenerateContentConfig(
        system_instruction="You are a concise programming assistant."
    )
)

print("\n--- AI Response ---")
print(response.text)
print("-------------------")c:\Users\LENOVO\Desktop\openai-api-lab\.env