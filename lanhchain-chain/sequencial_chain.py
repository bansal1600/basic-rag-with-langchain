# topic -> LLM -> report -> LLM -> Summary
# prompt1, promot2, model1, model2, parser

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()  # Load environment variables from .env file

promot1 = PromptTemplate(
    template="generate a report on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="generate a 5 pointer summary of the report from {report}",
    input_variables=["report"]
)

llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
parser = StrOutputParser()

chain = promot1 | llm | parser | prompt2 | llm | parser 

result = chain.invoke({'topic': 'Python programming'})
print(result)
