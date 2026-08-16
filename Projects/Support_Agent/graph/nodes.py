from langchain_openai import ChatOpenAI
from .state import SupportState

llm = ChatOpenAI(model="gpt-5.4-mini")

def route_query(state: SupportState) -> SupportState:
    latest_message = state["messages"][-1]

    response = llm.invoke(
        f"You are a strict quality-control reviewer. Rate 0 to 1 how confident you are "
        f"that a general support agent (not a specialist) can fully resolve this WITHOUT "
        f"needing account-specific data, billing system access, or human judgment. "
        f"Multi-part complaints, billing disputes, or contradictory information should "
        f"score LOW. Only respond with a number.\n\nQuestion: {latest_message}"
    )

    confidence_score = float(response.content.strip())

    return {"query": latest_message, "confidence": confidence_score}

def answer_query(state: SupportState) -> SupportState:
    latest_message = state["messages"][-1]

    response = llm.invoke(
        f"You are a helpful customer support agent. "
        f"Answer this customer's question clearly and concisely.\n\n"
        f"Question: {latest_message}"
    )

    assistant_reply = response.content

    return {"messages": [assistant_reply], "resolved": True}


def escalate_to_human(state: SupportState) -> SupportState:
    latest_message = state["messages"][-1]

    response = llm.invoke(
        f"You are a support agent triage assistant. This question needs to be "
        f"escalated to a human agent. Write a brief handoff summary for the human "
        f"agent explaining what the customer needs.\n\n"
        f"Question: {latest_message}"
    )

    handoff_message = (
        "I'm connecting you with a human agent who can better assist you. "
        f"Handoff summary: {response.content}"
    )

    return {"messages": [handoff_message], "escalated": True}