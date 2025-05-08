from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path=r"document-loaders\data",
    glob="*.pdf",
    show_progress=True,
    loader_cls="PyPDFLoader",
)

docs = loader.load()
print(f"Loaded {len(docs)} documents from the directory.")