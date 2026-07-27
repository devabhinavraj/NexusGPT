from langchain_community.vectorstores import FAISS

def create_vector_store(chunks , embeddings_model):
    vector_store = FAISS.from_documents(
        documents= chunks,
        embedding= embeddings_model
    )
    return vector_store