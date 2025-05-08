from langchain_community.document_loaders import TextLoader

loader = TextLoader(r"document-loaders\data\resume.txt", encoding="utf-8")

docs = loader.load()
print(type(docs)) # always a list of Document objects
print(len(docs)) # number of documents loaded
print(type(docs[0])) # Document object
print(docs[0].page_content) # content of the document
print(docs[0].metadata) # metadata of the document
print(docs[0].metadata["source"]) # source of the document
