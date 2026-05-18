from fastapi import FastAPI
from pydantic import BaseModel

from app.graphs.main_graph import graph

app = FastAPI()


class ChatRequest(BaseModel):
    user_query: str


@app.get("/")
def home():
    return {"message": "Backend is running"}


@app.post("/chat")
def chat(request: ChatRequest):

    result = graph.invoke({
        "user_query": request.user_query,
        "intent": "",
        "retrieved_context": "",
        "response": "",
        "next_node": "",
        "history": []
    })

    return result
