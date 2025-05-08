from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

prompt = PromptTemplate(
    template="write a jon about {topic}",
    input_variables=["topic"],
)

llm = ChatOpenAI()
parser = StrOutputParser()

runnable = RunnableSequence(
    prompt,
    llm,
    parser,
)

result = runnable.invoke({"topic": "AI"})
print(result)  # Output: "AI is a field of computer science that focuses on creating intelligent machines that can perform tasks that typically require human intelligence. It encompasses various subfields, including machine learning, natural language processing, and robotics. AI has the potential to revolutionize industries such as healthcare, finance, and transportation by automating processes and providing insights from large datasets."
