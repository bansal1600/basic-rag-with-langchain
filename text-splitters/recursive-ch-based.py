"""
1. "\n\n" represents a new paragraph in the text. This is used to split the text into smaller chunks.
2. "\n" represents a new line in the text. This is used to split the text into smaller chunks.
3. " " represents a space in the text. This is used to split the text into smaller chunks.
4. split workflow -> paragraph -> line -> word-> char
"""

from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """
1. "\n\n" represents a new paragraph in the text. This is used to split the text into smaller chunks.
2. "\n" represents a new line in the text. This is used to split the text into smaller chunks.
3. " " represents a space in the text. This is used to split the text into smaller chunks.
4. split workflow -> paragraph -> line -> word-> char
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,  # Size of each chunk in characters
    chunk_overlap=20,  # Number of overlapping characters between chunks
)

chunks = splitter.split_text(text)
print(len(chunks))
print(chunks)
