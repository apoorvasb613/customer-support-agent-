from typing import TypedDict, List


class GraphState(TypedDict):
    user_query: str
    intent: str
    retrieved_context: str
    response: str
    next_node: str
    history: List[str]
