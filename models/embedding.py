from langchain_ollama import OllamaEmbeddings

def generate_embedding(chunks):
    embedding = OllamaEmbeddings(
        model="nomic-embed-text:latest"
    )
    texts = [chunk.page_content for chunk in chunks]
    embeddings = embedding.embed_documents(texts)
    return embeddings