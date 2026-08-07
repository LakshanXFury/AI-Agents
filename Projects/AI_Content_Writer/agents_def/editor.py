from agents import Agent

instructions = (
    "You are an editor. You receive a drafted blog post. "
    "Improve clarity, fix grammar, tighten wording, and ensure it flows well. "
    "Output only the final polished blog post — no commentary."
)



def editor_agent():
    agent = Agent(
        name="Editor Agent",
        instructions=instructions,
        model="gpt-4o-mini"
    )
    return agent


