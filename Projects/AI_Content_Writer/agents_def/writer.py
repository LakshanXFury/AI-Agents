# Handoff from Editor


from agents import Agent
from agents_def.editor import editor_agent

instructions=(
        "You are a blog writer. You receive a content outline/plan. "
        "Write a full first-draft blog post based on it — clear structure, engaging tone. "
        "Once done, hand off to the Editor agent to polish it."
    )


def writer_agent():
    agent = Agent(
    name="Writer Agent",
    instructions=instructions,
    handoffs=[editor_agent()],
    model="gpt-4o-mini",
    )
    return  agent