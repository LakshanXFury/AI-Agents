from agents import Agent
from agents_def.file_writer import file_writer

instructions = (
    "You are an editor. You receive a drafted blog post. "
    "Improve clarity, fix grammar, tighten wording, and ensure it flows well. "
    "You MUST complete these steps in order: "
    "1. Edit and polish the FULL blog post. "
    "2. ALWAYS hand off the complete polished content to the File Writer Agent. "
    "You are FORBIDDEN from ending your turn without handing off to File Writer Agent. "
    "NEVER summarize or shorten the content. "
    "NEVER say 'content has been transferred' without actually doing the handoff. "
    "Your final action MUST be a handoff to File Writer Agent with the FULL content."
)



def editor_agent():
    agent = Agent(
        name="Editor Agent",
        instructions=instructions,
        model="gpt-5.4-mini",
        handoffs=[file_writer]
    )
    return agent


