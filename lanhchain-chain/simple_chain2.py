from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema


load_dotenv()  # Load environment variables from .env file

# Step 1: Define response schema
question_schema = ResponseSchema(name="Facts", description="5 interesting facts about the topic")

parser = StructuredOutputParser.from_response_schemas([question_schema])

# Step 2: Get format instructions
format_instructions = parser.get_format_instructions()

# Step 3: Define the prompt
prompt = PromptTemplate(
    template="Generate 5 interesting facts about {topic}.\n{format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": format_instructions}
)

# Step 4: Model and Chain
model = ChatOpenAI()
chain = prompt | model | parser

# Step 5: Run
result = chain.invoke({"topic": "Python programming"})
print(result)