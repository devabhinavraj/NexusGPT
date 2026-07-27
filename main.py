## Import the functions
from loaders.pdf_loaders import load_pdf
from rag.chunking import create_chunks
from models.embedding import get_embedding
from models.vector_store import create_vector_store
from rag.retriever import get_retriever
from models.llm import get_llm
from rag.prompt import get_prompt
from rag.document_chain import get_doc_chain
from rag.retrieval_chain import get_retrieval_chain


def main():
    # Load PDF
    documents = load_pdf()

    # Create Chunks
    chunks = create_chunks(documents)

    # Load Embedding Model
    embedding_model = get_embedding()

    # Create Vector Store
    vector_store = create_vector_store(chunks, embedding_model)

    # Create Retriever
    retriever = get_retriever(vector_store)

    # Load LLM
    model = get_llm()

    # Load Prompt
    prompt = get_prompt()

    # Create Document Chain
    chain = get_doc_chain(model, prompt)

    # Create Retrieval Chain
    retrieval_chain = get_retrieval_chain(retriever, chain)

    # User Query
    query = input("Enter your Query: ")

    # Get Answer
    result = retrieval_chain.invoke(
        {
            "input": query
        }
    )

    print(f"\nQuery: {query}")
    print(f"NexusGPT: {result['answer']}")


if __name__ == "__main__":
    main()