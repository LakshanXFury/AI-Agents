from typing import TypedDict, Annotated
import operator

class SupportState(TypedDict):
    messages: Annotated[list, operator.add]   # accumulates conversation history
    query: str
    confidence: float
    resolved: bool
    escalated: bool