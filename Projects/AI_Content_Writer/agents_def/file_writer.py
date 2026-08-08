from write_data import write_data
from agents import Agent


instructions = (
    "You receive the final polished blog post from the Editor Agent. "
    "Use the write_data tool to save the content into a file. "
    "Make sure the content is in Markdown format. "
    "Do not modify the content — write it exactly as received."
)


file_writer = Agent(
    name="File Writer Agent",
    tools=[write_data],
    instructions=instructions,
    model="gpt-5.4-mini",
)