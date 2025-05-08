from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://medium.com/p/2b7d1777b250")

docs = loader.load() # load everything in the pdf at once in memory

print(len(docs))  # Number of documents loaded
print(docs[0].page_content)  # Content of the first document