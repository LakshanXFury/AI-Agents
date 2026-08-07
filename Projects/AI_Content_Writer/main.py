import asyncio
from dotenv import load_dotenv
from agents import Runner, trace
from agents_def.planner import planner_agent


load_dotenv(override=True)


async def main():
    topic = input("What should be the Blog Post be about ? ")

    with trace("AI Conent Writer Pipeline"):
        result = await Runner.run(
            starting_agent=planner_agent(),
            input=topic,
            max_turns=20
        )
        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())