from agents.mcp import MCPServerStdio
import asyncio
from agents import Agent, Runner, trace
from dotenv import load_dotenv

load_dotenv(override=True)


# import pushover_fn

instructions = "You are able to answer the given question and also make sure to send push notification of the final result"
model="gpt-5.4-mini"

async def mcp_server():
    params = {"command": "uv", "args": ["run", "MCP/Pushover_MCP/pushover_fn.py"]}
    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as server:
        mcp_tools = await server.list_tools()
        print(mcp_tools)


async def main():

    input_data = input("Ask any question that you need answer for : ")
    params = {"command": "uv", "args": ["run", "MCP/Pushover_MCP/pushover_fn.py"]}

    async with MCPServerStdio(params=params, client_session_timeout_seconds=30) as mcp_server:
        agent = Agent(name="Researcher", instructions=instructions, model=model, mcp_servers=[mcp_server])
        with trace("Pushover_Agent"):
            result = await Runner.run(agent, input_data)
            print(result.final_output)


async def run_all():
    await mcp_server()  # list tools first
    await main()        # then run main



# if __name__ == "__main__":
#     asyncio.run(main(), mcp_server())


if __name__ == "__main__":
    asyncio.run(run_all())