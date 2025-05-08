from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

# Now access the API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key is not set. Please set it in your .env file.")

# Step 2: Load documents
documents = [
    "Python is a great programming language for data science.",
    "Laptops with high RAM and GPU are good for machine learning.",
    "JavaScript is popular for web development.",
    "MacBooks are preferred by many software engineers."
]

# Step 3: Create embedding model
embedding_model = OpenAIEmbeddings(api_key=api_key)

# Step 4: Store embeddings in FAISS vector store using from_texts
vector_db = FAISS.from_texts(documents, embedding_model)

# Step 5: User query
query = "Which laptop is best for AI projects?"

# Step 6: Search for the most relevant document
search_result = vector_db.similarity_search(query, k=1)

# Step 7: Print result
print("Top result:", search_result[0].page_content)
