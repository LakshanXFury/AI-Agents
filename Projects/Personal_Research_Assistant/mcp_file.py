from agents.mcp import MCPServerStdio  

fetch_params = {"command": "mcp-server-fetch", "args": []}
playwright_params = {
    "command": "npx",
    "args": ["@playwright/mcp@latest"]
}
TIMEOUT = 60




def research_mcp() -> list[MCPServerStdio]:
    fetch = MCPServerStdio(
        params=fetch_params,
        client_session_timeout_seconds=TIMEOUT
    )
    playwright = MCPServerStdio(
        params=playwright_params,
        client_session_timeout_seconds=TIMEOUT
    )

    return [fetch, playwright]

