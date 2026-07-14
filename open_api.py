from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(override=True)

openai = OpenAI()

# messages = [{"role": "user", "content": "What is 2+2?"}]
input_data = input("Ask any question that you need answer for : ")
messages = [{"role": "user", "content": input_data}]

response = openai.chat.completions.create(
    model="gpt-4o-mini",  # ✅ Valid model name
    messages=messages
)

print(response.choices[0].message.content)