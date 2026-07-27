from langchain_ollama import ChatOllama

def get_llm():
    model= ChatOllama(
        model= "qwen2.5:7b",
        temperature= 0
    )
    return model