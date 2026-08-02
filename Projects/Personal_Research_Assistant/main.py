from agents import Agent, Runner, trace, WebSearchTool
from agents.mcp import MCPServerStdio  
import asyncio
from dotenv import load_dotenv
load_dotenv(override=True)

# fetch_params = {"command": "mcp-server-fetch", "args": []}

# async def main():

#     async with MCPServerStdio(params=fetch_params, client_session_timeout_seconds=60) as server:
#         fetch_tools = await server.list_tools()
#         print(fetch_tools)

# asyncio.run(main())

instructions=(
    "Research the given topic using web search and answer in a single clear paragraph. "
    "Do not include any markdown links, citation brackets, or source URLs inline in the paragraph. "
    "Do not prefix the answer with anything. Start directly with the answer. "
    "If you want to mention sources, list them as plain text titles in a separate 'Sources:' line after the paragraph."
)

async def main():

    input_data = input("Ask any question that you need answer for : ")

    agent = Agent(
        name="Research Assistant",
        instructions=instructions,
        tools=[WebSearchTool()],
        model="gpt-4o-mini",
    )

    with trace("Personal Research Assistant"):
        result = await Runner.run(agent, input_data, max_turns=20)
        print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())