from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

llm  = HuggingFaceEndpoint(
    repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"), 
)

model = ChatHuggingFace(llm=llm, temperature=0.7, max_length=512)
result = model.invoke("What is the capital of France?") 
print(result.content)  # Output: "The capital of France is Paris."



 
 