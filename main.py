## Import the functions
import os
from loaders.pdf_loaders import load_pdf
from rag.chunking import create_chunks
from models.embedding import get_embedding
from models.vector_store import create_vector_store
from rag.retriever import get_retriever
from models.llm import get_llm
from rag.prompt import get_prompt
from rag.document_chain import get_doc_chain
from rag.retrieval_chain import get_retrieval_chain
from models.vector_store import save_vector_local
from models.vector_store import load_vector_local


def main():

    # Load Embedding Model
    embedding_model = get_embedding()

    db_path = "vector_database"

    # Check if Vector Store already exists
    if os.path.exists(db_path):

        print("Loading existing Vector Store...")

        vector_store = load_vector_local(
            db_path,
            embedding_model
        )

    else:

        print("Creating new Vector Store...")

        # Load PDF
        documents = load_pdf()
        print("="*80)
        print("DOCUMENTS PAGE CONTENET")
        print("="*80)
        print(documents[0].page_content[:4000])
        print("="*80)

        # Create Chunks
        chunks = create_chunks(documents)

        # Create Vector Store
        vector_store = create_vector_store(
            chunks,
            embedding_model
        )

        # Save Vector Store
        save_vector_local(
            vector_store,
            db_path
        )

    # Create Retriever
    retriever = get_retriever(vector_store)

    # Load LLM
    model = get_llm()

    # Load Prompt
    prompt = get_prompt()

    # Create Document Chain
    chain = get_doc_chain(model, prompt)

    # # Create Retrieval Chain
    # retrieval_chain = get_retrieval_chain(retriever, chain)

    
    query = input("Ask NexusGPT...")

    # -------------------------
    # Debug: Retrieved Chunks
    # -------------------------
    docs = retriever.invoke(query)

    print("\n" + "=" * 80)
    print("Retrieved Chunks")
    print("=" * 80)

    for i, doc in enumerate(docs):
        print(f"\nChunk {i+1}")
        print(doc.page_content)
        print("-" * 80)

    # -------------------------
    # RAG Answer
    # -------------------------
    retrieval_chain = get_retrieval_chain(retriever, chain)

    result = retrieval_chain.invoke(
        {
            "input": query
        }
    )

    print("\nNexusGPT:", result["answer"])

    # # User Query
    # while True:
    #     query = input("Ask NexusGPT...")
    #     if query.lower().strip() == "exit":
    #         print("Thank you for using NexusGPT! ❤️\n")
    #         break
    #     # Get Answer
    #     result = retrieval_chain.invoke(
    #         {
    #             "input": query
    #         }
    #     )
    #     print(f"NexusGPT: {result['answer']}\n")


if __name__ == "__main__":
    main()