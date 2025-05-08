from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a:int = Field(required = True, description="the First number to add")
    b:int = Field(required = True, description="the Second number to add")

class MultiplyTool(BaseTool):
    name: str = "multiply",
    description: str = "multiply two numbers",
    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a:int, b:int) -> int: # typehinting tells what datatypes
        return a * b

multiply_tool = MultiplyTool()
result = multiply_tool.invoke({'a':3, 'b':3})

print(result) # invoke custom fnction
print(multiply_tool.name) # print function name
print(multiply_tool.description)
print(multiply_tool.args)
print(multiply_tool.args_schema.model_json_schema())
