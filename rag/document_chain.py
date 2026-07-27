from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain,
)
def get_doc_chain(model, prompt):
    chain = create_stuff_documents_chain(model , prompt)
    return chain
