from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader, PyMuPDFLoader

UPLOAD_DIR = Path(__file__).resolve().parent.parent / "data" / "uploads"


def load_pdf():
    dir_loader = DirectoryLoader(
        str(UPLOAD_DIR),
        glob="**/*.pdf",
        loader_cls=PyMuPDFLoader,
        show_progress=False,
    )
    pdf_documents = dir_loader.load()
    return pdf_documents


if __name__ == "__main__":
    pdf_documents = load_pdf()
    print(f"Total pages loaded: {len(pdf_documents)}")
