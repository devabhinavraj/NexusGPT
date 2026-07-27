from langchain_community.vectorstores import FAISS

def create_vector_store(chunks , embeddings_model):
    vector_store = FAISS.from_documents(
        documents= chunks,
        embedding= embeddings_model
    )
    return vector_store

def save_vector_local(vector_store ,db_path):
    vector_store.save_local(db_path)

def load_vector_local(db_path , embedding):
    vector_database = FAISS.load_local(
        db_path,
        embedding,
        allow_dangerous_deserialization=True
    )
    return vector_database