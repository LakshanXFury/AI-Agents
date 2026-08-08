# Handoff from Editor


from agents import Agent
from agents_def.editor import editor_agent

instructions = (
    "You are the Writer Agent. "
    "Your ONLY job is to write a complete first draft of the blog post based on the outline provided. "
    "After writing the draft, you MUST immediately hand off to the Editor Agent. "
    "You are FORBIDDEN from ending your turn without handing off. "
    "NEVER return the draft to the user directly. "
    "ALWAYS transfer to editor_agent as your final action."
)


def writer_agent():
    agent = Agent(
    name="Writer Agent",
    instructions=instructions,
    handoffs=[editor_agent()],
    model="gpt-5.4-mini",
    )
    return  agent