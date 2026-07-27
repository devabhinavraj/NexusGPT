from langchain_ollama import OllamaEmbeddings

def get_embedding():
    embeddings_model = OllamaEmbeddings(
        model="nomic-embed-text:latest"
    )
    return embeddings_model