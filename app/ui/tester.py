from fastapi import FastAPI

from app.app import ChatRequest
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
@app.post("/chat")
def chat(request: ChatRequest):

    result = cn_graph.invoke({
        "user_query": request.user_query,
        "intent": "",
        "retrieved_context": "",
        "response": "",
        "next_node": "",
        "history": []
    })
    return result