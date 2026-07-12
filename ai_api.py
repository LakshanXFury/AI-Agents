from openai import OpenAI
from dotenv import load_dotenv
import os

# Automatically finds OPENAI_API_KEY from environment
load_dotenv(override=True) #This reads your .env file and loads the key into your system's environment variables behind the scenes

openai_api_key = os.getenv('OPENAI_API_KEY')

client_ai = OpenAI()


messages = [{"role": "user", "content": "What is 2+2?"}]

response = client_ai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)

question = response.choices[0].message.content

print(question)