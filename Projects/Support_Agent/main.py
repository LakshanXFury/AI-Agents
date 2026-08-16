from dotenv import load_dotenv
load_dotenv(override=True)

from graph.build_graph import graph

config = {"configurable": {"thread_id": "user-session-1"}}
print("I am a Support Agent, As your questions. (Type Exit or Quit to close the agent)")

while True:
    user_input = input("You: ")
    if user_input.lower() in ("quit", "exit"):
        break
    result = graph.invoke({"messages": [user_input]}, config=config)
    print("Bot:", result["messages"][-1])