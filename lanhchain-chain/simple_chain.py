from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()  # Load environment variables from .env file

promt = PromptTemplate(
    template="generate 5 interesting questions about {topic}",
    input_variables= ["topic"]
)
model = ChatOpenAI()
parser = StrOutputParser()

chain = promt | model | parser

result = chain.invoke({'topic' : 'Python programming'})
print(result)