from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

loader = PyPDFLoader("data\dl-curriculum.pdf")

docs = loader.load()

text_splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=20,
    separator=""
)

result = text_splitter.split_documents(docs)
print("Number of chunks:", len(result))
print(result[0].page_content)  