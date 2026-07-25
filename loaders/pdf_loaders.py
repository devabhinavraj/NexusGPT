from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyMuPDFLoader 

dir_loader = DirectoryLoader(
    "C:/Users/win11/Desktop/NexusGPT/data/uploads",
    glob="**/*.pdf",
    loader_cls=PyMuPDFLoader,
    show_progress= False
)
pdf_documents = dir_loader.load()
print(len(pdf_documents))






