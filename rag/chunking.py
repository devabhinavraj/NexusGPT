import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from langchain_text_splitters import RecursiveCharacterTextSplitter
from loaders.pdf_loaders import load_pdf

def create_chunks(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=50,
        length_function=len,
        is_separator_regex=False,
    )
    chunks = text_splitter.split_documents(documents)
    return chunks


if __name__ == "__main__":
    chunks_pdf = create_chunks(load_pdf())
    print(f"Total Chunks loaded: {len(chunks_pdf)}")