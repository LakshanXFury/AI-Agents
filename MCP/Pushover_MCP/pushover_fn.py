from dotenv import load_dotenv
import os
import requests

from mcp.server.fastmcp import FastMCP

load_dotenv(override=True)
mcp = FastMCP("pushover_server")

pushover_user = os.getenv("PUSHOVER_USER")
pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_url = "https://api.pushover.net/1/messages.json"


@mcp.tool()
def push(message:str):
    """
    Send a Push notification using the pushover feature.

    Args:
        message: The message that you want to send.
    """
    print(f"Push: {message}")
    payload = {"user": pushover_user, "token": pushover_token, "message": message}
    requests.post(pushover_url, data=payload)


if __name__ == "__main__":
    mcp.run(transport="stdio")