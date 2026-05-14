from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="mistral"
)


def ask_llm(prompt):

    response = llm.invoke(prompt)

    return response.content
