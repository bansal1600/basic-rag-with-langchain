# making tool is a 3 step process:
# 1. Import the tools you need from langchain_community.tools
# 2. Create the tool or custom function + add @tool + typehinting + docstring

from langchain_core.tools import tool

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




