from app.services.llm_service import ask_llm
from .dummy_data import FAQ_DATA
from .tools import get_order_status


def intent_node(state):

    query = state["user_query"].lower()

    if "refund" in query:
        state["intent"] = "faq"

    elif "order" in query:
        state["intent"] = "order"

    else:
        state["intent"] = "unknown"

    return state


def retrieval_node(state):

    query = state["user_query"].lower()

    for key, value in FAQ_DATA.items():

        if key in query:
            state["retrieved_context"] = value

    return state


def order_lookup_node(state):

    query = state["user_query"]

    words = query.split()

    order_id = None

    for word in words:

        if word.isdigit():
            order_id = word
            break

    if order_id:

        status = get_order_status(order_id)

        state["retrieved_context"] = (
            f"Order {order_id} status is {status}"
        )

    else:
        state["retrieved_context"] = (
            "No order ID found"
        )

    return state


def response_node(state):

    prompt = f"""
    You are a customer support assistant.

    Customer Query:
    {state['user_query']}

    Context:
    {state.get('retrieved_context', '')}

    Generate a helpful response.
    """

    response = ask_llm(prompt)

    state["response"] = response

    return state
