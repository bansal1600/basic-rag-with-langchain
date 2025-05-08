from langchain_core.tools import tool

#step1 cretae a custom function
@tool #make llm can communicate with this function
def multiply(a:int, b:int) -> int: # typehinting tells what datatypes
    """Multiplies two numbers.""" #docstring helps llm to understand what this function do
    return a * b

@tool #make llm can communicate with this function
def add(a:int, b:int) -> int: # typehinting tells what datatypes
    """add two numbers.""" #docstring helps llm to understand what this function do
    return a + b

class MathtoolKit: # need to make a class to add all the tools to access them later
    def get_tools(self):
        return [add, multiply]
    
toolkit = MathtoolKit()
tools = toolkit.get_tools()

for tool in tools:
    print(tool.name, "=>", tool.description)