from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
from langchain.schema import Document

load_dotenv()  # Load environment variables from .env file

#create example document to store in vector store with metadata

doc1 =  Document(
    page_content="Python is a great programming language for data science.", 
    metadata={"source": "doc1"}
    )
doc2 =  Document(
    page_content="Laptops with high RAM and GPU are good for machine learning.", 
    metadata={"source": "doc2"}
    )
doc3 =  Document(
    page_content="JavaScript is popular for web development.", 
    metadata={"source": "doc3"}
    )
doc4 =  Document(
    page_content="MacBooks are preferred by many software engineers.", 
    metadata={"source": "doc4"}
    )
doc5 =  Document(
    page_content="Python is a versatile language used in various domains.", 
    metadata={"source": "doc5"}
    )

docs= [doc1, doc2, doc3, doc4, doc5]

vector_db = Chroma(
    embedding_function=OpenAIEmbeddings(), #embedding function to use for vector store
    persist_directory="my_chroma_db", #directory to persist the vector store
    collection_name="sample" #name of the collection in the vector store
)

vector_db.add_documents(docs) #add documents to the vector store
print("Documents added to vector store.")

result = vector_db.get(include=["embeddings","documents", "metadatas"]) #get all documents from the vector store
# print(result) #print the result

#similarity search
query = "Which laptop is best for AI projects?" #user query
search_result = vector_db.similarity_search_with_score(query, k=1) #search for the most relevant document
 
print("Top result:", search_result[0][0].page_content) #print the result