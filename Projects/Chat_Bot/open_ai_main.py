from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(override=True)

openai = OpenAI()
model="gpt-5.4-mini"

# 1. INITIALIZE HISTORY: Create an ongoing conversation list outside the loop
conversation_history = [
    {
        "role": "system", 
        "content": "You are a helpful assistant. Give clear, scannable answers using short sentences and bullet points for lists. DO NOT use Markdown or stars (**) for bolding text. Print only raw text."
    }
]

print("Chatbot initialized! Type 'quit' to exit.\n")

while True:
    input_message = input("Ask any question that you need answer for ? (If you dont have any question type quit): ")

    if input_message.strip().lower() == "quit":
        break
    else:
        # 2. RECORD USER INPUT: Append what you just typed into the history
        conversation_history.append({"role": "user", "content": input_message})

        # 3. SEND FULL HISTORY: Pass the entire accumulated list, not just a single prompt
        
        response = openai.chat.completions.create(
            model= model,
            messages=conversation_history
        )
        ai_answer = response.choices[0].message.content
        print("\n" + ai_answer + "\n")

        # 4. RECORD AI RESPONSE: Save what the AI said so it remembers its own context next time!
        conversation_history.append({"role": "assistant", "content": ai_answer})


