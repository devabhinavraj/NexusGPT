from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyMuPDFLoader 
from pathlib import Path
UPLOAD_DIR = Path("data/uploads")

def load_pdf():
    dir_loader = DirectoryLoader(
        UPLOAD_DIR,
        glob="**/*.pdf",
        loader_cls= PyMuPDFLoader,
        show_progress= False
    )
    pdf_documents = dir_loader.load()
    return pdf_documents


if __name__ == "__main__":
    pdf_documents = load_pdf()
    print(f"Total pages loaded: {len(pdf_documents)}")






