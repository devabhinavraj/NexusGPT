from loaders.pdf_loaders import load_pdf
from rag.chunking import create_chunks
from models.embedding import get_embedding
from models.vector_store import create_vector_store

def main():
    documents = load_pdf()
    chunks = create_chunks(documents)
    embedding_model = get_embedding()
    vector_store = create_vector_store(chunks , embedding_model)

    print(f"Total Documents: {len(documents)}")
    print(f"Total Chunks: {len(chunks)}")
    print("Vector Store Created Successfully")

if __name__ == "__main__":
    main()