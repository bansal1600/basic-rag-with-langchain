from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from langchain.schema.runnable import RunnableParallel

load_dotenv()  # Load environment variables from .env file

model1 = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model2 = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt1 = PromptTemplate(
    template="generate short and simple notes on {topic}  in  100 words",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="generate 2 short question & answer on {topic} in 50 words",
    input_variables=["topic"]
)
prompt3 = PromptTemplate(
    template="merge the provided notes and quiz into a single document \n notes: {notes} \n quiz: {quiz}",
    input_variables=["notes", "quiz"]
)

parser = StrOutputParser()

#create a pararallel chain
parallel_chian = RunnableParallel({
    'notes' : prompt1 | model1 | parser,
    'quiz' : prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chian | merge_chain

topic = 'Python programming'
result = chain.invoke({'topic': topic})
print(result)
