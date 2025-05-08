from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key is not set. Please set it in your .env file.")

embedding = OpenAIEmbeddings(api_key=api_key, model="text-embedding-ada-002")
result = embedding.embed_query("What is the capital of France?")

print(result)