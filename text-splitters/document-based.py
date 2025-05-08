#there are other document based text splitters in the langchain library like markdown, csv, json, etc.

from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = """"
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"

student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=20
)

chunks = splitter.split_text(text)

print(len(chunks))  # Output: 3
print(chunks)