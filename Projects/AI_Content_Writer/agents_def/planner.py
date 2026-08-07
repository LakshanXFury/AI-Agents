from agents import Agent
from agents_def.writer import writer_agent

instructions = (
     "You are a content planner. Given a topic, create a clear outline: "
     "a title, 3-5 section headers, and one line describing what each section covers. "
     "Once the outline is ready, hand off to the Writer agent to draft the full post."
)


def planner_agent():
    agent = Agent(
    name="Planner Agent",
    instructions=instructions,
    handoffs=[writer_agent()],
    model="gpt-4o-mini",
    )
    return  agent