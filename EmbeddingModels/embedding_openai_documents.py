from langchain_openai import OpenAIEmbeddings
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
embedding_model = OpenAIEmbeddings(api_key=api_key, dimensions=32)

result = embedding_model.embed_documents(documents)
print(result)  # Output: Embedding vectors for the documents
