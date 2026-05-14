def route_intent(state):

    intent = state["intent"]

    if intent == "faq":
        return "retrieval"

    elif intent == "order":
        return "order_lookup"

    return "response"
