from langchain_classic.chains import (
    create_retrieval_chain ,
)

def get_retrieval_chain(retriver , chain):
    retriever_chain = create_retrieval_chain(
        retriver , chain
    )
    return retriever_chain