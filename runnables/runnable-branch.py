from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough, RunnableSequence, RunnableParallel, RunnableLambda, RunnableBranch
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()  

promot1 = PromptTemplate(
        template="genrate a report about {topic} in 250 words",
        input_variables= ["topic"],
)

promot2 = PromptTemplate(
        template="summarize the following text {text} in 100 words",
        input_variables= ["text"],
)

llm = ChatOpenAI()
parser = StrOutputParser()

runnable1 = RunnableSequence(promot1, llm, parser)

brach_chain = RunnableBranch(
    (lambda x:len(x.split()) > 200, RunnableSequence(promot2, llm, parser)),
    RunnablePassthrough(),
)

final_chain = RunnableSequence(runnable1, brach_chain)

result = final_chain.invoke({"topic": "AI in healthcare"})
print(result)