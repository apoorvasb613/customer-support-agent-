from fastapi import FastAPI

from app.graphs.cn.cn_graph import cn_graph


app = FastAPI()


@app.get("/test/{node_name}")

def test_node(
    node_name: str,
    query: str
):

    result = cn_graph.invoke({

        "user_query": query,

        "intent": "",

        "retrieved_context": "",

        "response": "",

        "next_node": "",

        "history": []

    })

    return result
