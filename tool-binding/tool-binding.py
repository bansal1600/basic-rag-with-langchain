# making tool is a 3 step process:
# 1. Import the tools you need from langchain_community.tools
# 2. Create the tool or custom function + add @tool + typehinting + docstring

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

result = multiply.invoke({"a":4, "b":5})

print(result) # invoke custom fnction
print(multiply.name) # print function name
print(multiply.description)
print(multiply.args)
print(multiply.args_schema.model_json_schema())

#tool binding process
llm = ChatOpenAI()
llm_with_tools = llm.bind_tools([multiply])

print(llm_with_tools)

#tool calling
# print(llm_with_tools.invoke('Hi How are you?'))
# print(llm_with_tools.invoke('can you multiply 2 by 3')) # automatically suggests which tools to call is called as Tool Calling
print(llm_with_tools.invoke('can you multiply 2 by 3').tool_calls[0])

(multiply.invoke(
    {'name': 'multiply',
      'args': {'a': 2, 'b': 3},
        'id': 'call_4TCm2KarY6UMwZ2wjsebGJOZ',
          'type': 'tool_call'}
          ))





