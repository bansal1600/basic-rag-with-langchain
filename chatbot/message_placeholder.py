from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import os

# chat template
chat_template = ChatPromptTemplate.from_messages([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []

# get current script's folder
script_dir = os.path.dirname(os.path.abspath(__file__))
chat_history_path = os.path.join(script_dir, 'chat_history.txt')

chat_history = []

if os.path.exists(chat_history_path):
    with open(chat_history_path, 'r') as f:
        chat_history.extend(f.readlines())
else:
    print(f"Warning: '{chat_history_path}' not found. Starting with an empty chat history.")

# create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})

print(prompt)