from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"document-loaders\data\dl-curriculum.pdf")
docs = loader.load() # load everything in the pdf at once in memory
lazy_docs = loader.lazy_load() # load lazily(only on demand), only loads the first page in memory

print(len(docs))  # Number of documents loaded
print(docs[0].page_content)  # Content of the first document
print(docs[0].metadata)  # Metadata of the first document


#refer https://python.langchain.com/docs/com for more details