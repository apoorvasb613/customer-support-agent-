from langgraph.graph import StateGraph, END

from .state import GraphState

from .nodes import (
    intent_node,
    retrieval_node,
    order_lookup_node,
    response_node
)

from .edges import route_intent


builder = StateGraph(GraphState)


# ADD NODES

builder.add_node(
    "intent",
    intent_node
)

builder.add_node(
    "retrieval",
    retrieval_node
)

builder.add_node(
    "order_lookup",
    order_lookup_node
)

builder.add_node(
    "response",
    response_node
)


# ENTRY POINT

builder.set_entry_point("intent")


# CONDITIONAL EDGES

builder.add_conditional_edges(
    "intent",
    route_intent,
    {
        "retrieval": "retrieval",
        "order_lookup": "order_lookup",
        "response": "response"
    }
)


# NORMAL EDGES

builder.add_edge(
    "retrieval",
    "response"
)

builder.add_edge(
    "order_lookup",
    "response"
)

builder.add_edge(
    "response",
    END
)


# COMPILE GRAPH

cn_graph = builder.compile()
