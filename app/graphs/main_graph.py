import json

from app.graphs.cn.cn_graph import cn_graph


result = cn_graph.invoke({

    "user_query": "Where is my order 101?",

    "intent": "",

    "retrieved_context": "",

    "response": "",

    "next_node": "",

    "history": []

})


print("\nFINAL GRAPH OUTPUT:\n")

print(
    json.dumps(
        result,
        indent=4
    )
)
