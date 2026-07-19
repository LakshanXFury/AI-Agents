from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(override=True)

openai = OpenAI()

messages = [
    {"role": "system", "content": "You are a helpful and concise sports expert. Answer shortly with few lines dont give detailed explanation."},
    {"role": "user", "content": "Who is Cristiano Ronaldo?"}
]

response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,

)

print(response.choices[0].message.content)