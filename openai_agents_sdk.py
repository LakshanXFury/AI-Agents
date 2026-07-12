import asyncio
from agents import Agent, Runner, trace
from dotenv import load_dotenv

load_dotenv(override=True)

agent = Agent(name="Jokester", instructions="You are a joke teller, who tells jokes", model="gpt-4o-mini")

user_input = input(str("Enter the Topic in which you want the Joke to be asked for: "))

async def main():
    with trace("Telling a Joke"):
        result = await Runner.run(agent, input=user_input)
        print(result.final_output)

asyncio.run(main())