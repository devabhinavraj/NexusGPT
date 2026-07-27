from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=50,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.split_documents(documents)
    return chunks