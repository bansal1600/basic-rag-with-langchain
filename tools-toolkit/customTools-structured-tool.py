from langchain.tools import StructuredTool
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a:int = Field(required = True, description="the First number to add")
    b:int = Field(required = True, description="the Second number to add")

def multiply_func(a:int, b:int) -> int: # typehinting tells what datatypes
    return a * b

multiply_tool = StructuredTool.from_function(
    func=multiply_func,
    name="multiply",
    description="multiply two numbers",
    args_schema=MultiplyInput
)

result = multiply_tool.invoke({'a':3, 'b':3})

print(result) # invoke custom fnction
print(multiply_tool.name) # print function name
print(multiply_tool.description)
print(multiply_tool.args)
print(multiply_tool.args_schema.model_json_schema())
