from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

load_dotenv()

#step1 cretae a custom function
@tool #make llm can communicate with this function
def multiply(a:int, b:int) -> int: # typehinting tells what datatypes
    """Multiplies two numbers.""" #docstring helps llm to understand what this function do
    return a * b

#tool binding process
llm = ChatOpenAI()
llm_with_tools = llm.bind_tools([multiply])

#tool calling
query = HumanMessage('can you multiply 2 by 3')
messages = [query]

result = llm_with_tools.invoke(messages)
messages.append(result)

tool_result = multiply.invoke(result.tool_calls[0])
messages.append(tool_result)

print(llm_with_tools.invoke(messages).content)





