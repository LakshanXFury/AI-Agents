from agents import Agent, Runner, trace, WebSearchTool
from agents.mcp import MCPServerStdio  
import asyncio
from dotenv import load_dotenv
load_dotenv(override=True)


instructions = """
You are a research assistant.

Use Fetch to retrieve webpage content whenever possible.

Use Playwright only when interaction is required (cookies, pop-ups, dynamic content, scrolling, navigation, or pages Fetch cannot read).

Navigate directly to the most relevant page instead of repeatedly searching.

Stop browsing as soon as you have enough information to answer confidently.

Answer in a clear, concise paragraph. Do not include markdown links, inline URLs, or citation brackets. If appropriate, end with:

Sources: Source 1; Source 2

"""

# MCP's

fetch_params = {"command": "mcp-server-fetch", "args": []}
playwright_params = {
    "command": "npx",
    "args": ["@playwright/mcp@latest"]
}


async def main():

    input_data = input("Ask any question that you need answer for : ")
    async with MCPServerStdio(params=fetch_params, client_session_timeout_seconds=60) as fetch_server:
        async with MCPServerStdio(params=playwright_params, client_session_timeout_seconds=60) as playwright_server: 

            agent = Agent(
                name="Research Assistant",
                instructions=instructions,
                # tools=[WebSearchTool()],
                mcp_servers=[fetch_server, playwright_server],
                model="gpt-4o-mini",
            )

            with trace("Personal Research Assistant"):
                result = await Runner.run(agent, input_data, max_turns=20)
                print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())







#### Only using Playwright ----------------------------

# instructions = """
# You are a research assistant.

# Use the Playwright browser tools.

# Navigate directly to the most relevant page.

# Read the page.

# Answer the user's question.

# Do not continue browsing after sufficient information has been gathered.

# Avoid repeated searches.

# Stop as soon as you can answer confidently.
# """

# print(instructions)

# async def main():

#     input_data = input("Ask any question that you need answer for : ")
#     async with MCPServerStdio(params=playwright_params, client_session_timeout_seconds=60) as playwright_server: 

#         agent = Agent(
#             name="Research Assistant",
#             instructions=instructions,
#                 # tools=[WebSearchTool()],
#             mcp_servers=[playwright_server],
#             model="gpt-4o-mini",
#         )

#         with trace("Personal Research Assistant"):
#             result = await Runner.run(agent, input_data, max_turns=20)
#             print(result.final_output)

# if __name__ == "__main__":
#     asyncio.run(main())