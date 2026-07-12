from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(override=True)

openai = OpenAI()

messages = [{"role": "user", "content": "What is 2+2?"}]

response = openai.chat.completions.create(
    model="gpt-4o-mini",  # ✅ Valid model name
    messages=messages
)

print(response.choices[0].message.content)