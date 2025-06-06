from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough, RunnableSequence, RunnableParallel, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

prompt1 = PromptTemplate(
    template="gerate a joke about {topic}",
    input_variables=["topic"],
)

llm = ChatOpenAI()
parser = StrOutputParser()

runnable1 = RunnableSequence(prompt1, llm, parser)

def parse_explanation(joke: str) -> str:
    return len(joke.split())

runnable2 = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "explanation": RunnableLambda(parse_explanation),
    }
)

final_chain = RunnableSequence(runnable1,runnable2,)

result = final_chain.invoke({"topic": "robots"})

print(result)  # Output: {'joke': 'Why did the robot go on a diet? Because it had too many bytes!', 'explanation': 'The joke plays on the word "bytes," which is a unit of digital information. It humorously suggests that the robot is concerned about its weight, just like a person might be, but in a techy way.'}