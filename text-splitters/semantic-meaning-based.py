from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

text_splitter = SemanticChunker(
    OpenAIEmbeddings(), 
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=0.75,  # Adjust this value based on your needs
)

text = """
    Python is a great programming language for data science. Laptops with high RAM and GPU are good for machine learning. JavaScript is popular for web development. MacBooks are preferred by many software engineers.
    terrorism is a major global issue that affects many countries. It involves the use of violence and intimidation, especially against civilians, to achieve political or
    
    Indian Premier League is a cricket league played in India. it is biggest cricket league watched all over the world. 
    """

chunks = text_splitter.split_text(text)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk}")

