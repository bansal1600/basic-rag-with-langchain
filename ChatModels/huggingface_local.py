from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os
from dotenv import  load_dotenv

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id= "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    pipeline_kwargs= {
        "temperature": 0.7
        , "max_length": 512
        }
)

model = ChatHuggingFace(llm = llm)
result = model.invoke("What is the capital of France?")
print(result.content)  # Output: "The capital of France is Paris."