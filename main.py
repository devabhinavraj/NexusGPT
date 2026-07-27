from loaders.pdf_loaders import load_pdf
from rag.chunking import create_chunks
from models.embedding import generate_embedding

def main():
    documents = load_pdf()
    chunks = create_chunks(documents)
    embeddings = generate_embedding(chunks)

    print(f"Total Documents: {len(documents)}")
    print(f"Total Chunks: {len(chunks)}")
    print(f"Total Embeddings: {len(embeddings)}" )


if __name__ == "__main__":
    main()