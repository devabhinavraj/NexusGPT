from loaders.pdf_loaders import load_pdf
from rag.chunking import create_chunks
from models.embedding import get_embedding
from models.vector_store import create_vector_store
from rag.retriever import get_retriever


def main():
    documents = load_pdf()
    chunks = create_chunks(documents)
    embedding_model = get_embedding()
    vector_store = create_vector_store(chunks , embedding_model)
    query = input("Enter yor Query:")
    retriever = get_retriever(vector_store)
    result = retriever.invoke(query)

    print(f"Total Documents: {len(documents)}")
    print(f"Total Chunks: {len(chunks)}")
    print("Vector Store Created Successfully")
    print(f"Query: {query} \n NexusGPT: {result[0].page_content}")

if __name__ == "__main__":
    main()