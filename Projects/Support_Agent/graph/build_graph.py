from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from .state import SupportState
from .nodes import route_query, answer_query, escalate_to_human

def confidence_router(state: SupportState) -> str:
    return "escalate" if state["confidence"] < 0.6 else "answer"

workflow = StateGraph(SupportState)
workflow.add_node("route", route_query)
workflow.add_node("answer", answer_query)
workflow.add_node("escalate", escalate_to_human)
    
workflow.add_edge(START, "route")
workflow.add_conditional_edges(
    "route",
    confidence_router,
    {"answer": "answer", "escalate": "escalate"},
)
workflow.add_edge("answer", END)
workflow.add_edge("escalate", END)

memory = MemorySaver()
graph = workflow.compile(checkpointer=memory)