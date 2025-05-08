from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
from langchain.schema import Document

load_dotenv()  # Load environment variables from .env file

#create example document to store in vector store with metadata

documents =  [
    Document(
    page_content="Python is a great programming language for data science.", 
    metadata={"source": "doc1"}
    ), 
    Document(
    page_content="Laptops with high RAM and GPU are good for machine learning.", 
    metadata={"source": "doc2"}
    ),
     Document(
    page_content="JavaScript is popular for web development.", 
    metadata={"source": "doc3"}
    ),
    Document(
    page_content="MacBooks are preferred by many software engineers.", 
    metadata={"source": "doc4"}
    )
]

vector_store = Chroma.from_documents(
    documents=documents,
    embedding=OpenAIEmbeddings(), #embedding function to use for vector store
    collection_name="sample", #name of the collection in the vector store
)

#convert vector store to a retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 2})

#print results
results = retriever.invoke("Which laptop is best for AI projects?") #user query

for i, doc in enumerate(results):
    print(f"\n---Results {i+1}---")
    print(doc.page_content)

results = vector_store.similarity_search("Which laptop is best for AI projects?", k=2) #user query
for i, doc in enumerate(results):
    print(f"\n---Results {i+1}---")
    print(doc.page_content)