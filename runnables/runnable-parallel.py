from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

prompt1 = PromptTemplate(
    template="gerate a tweet about {topic}",
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template="gerate a linkedin post about {topic}",
    input_variables=["topic"],
)

llm = ChatOpenAI()
parser = StrOutputParser()

parallel_chain = RunnableParallel(
  {
   "tweet" : RunnableSequence(prompt1, llm, parser),
   "linkedin" : RunnableSequence(prompt2, llm, parser),
  } 
 )

result = parallel_chain.invoke({"topic": "AI"})
print(result)  