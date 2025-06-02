# 🧠 LangChain Projects and Vector DB Exploration

Welcome to my personal repository where I dive deep into **LangChain**, **LLMs**, and **Vector Databases**. This repo showcases hands-on projects and code samples I’ve built while learning how to develop intelligent applications using **retrievers**, **chat models**, **embedding models**, and more.

---

## 📚 What I Learned

This repo is the outcome of my learning journey in:

- 🔗 LangChain Framework (Chains, Prompts, Tools)
- 💬 Chat Models with OpenAI/GPT
- 🧠 Embedding Models & Vector Similarity Search
- 📄 Document Loaders and Text Splitters
- 🗂️ Vector Databases (Chroma DB)
- 🛠️ Self-Query Retrievers & Custom Tool Bindings
- 🧱 Toolkits for Agent-like behaviors
- 🔎 Query Construction & Structured Filtering
- 🧪 Running chains and combining tools

---

## 📁 Folder Structure

| Folder/File         | Description |
|---------------------|-------------|
| `ChatModels/`       | Code to integrate and interact with chat models |
| `EmbeddingModels/`  | Code for generating embeddings from documents |
| `chatbot/`          | A chatbot interface using LangChain & LLMs |
| `data/`             | Sample documents for testing (PDFs, text files, etc.) |
| `document-loaders/` | Loaders to ingest different file types |
| `langchain-promots/`| Prompt templates for guiding LLMs |
| `langchain-chain/`  | Custom chain implementations |
| `my_chroma_db/`     | Local Chroma DB setup with stored vectors |
| `project/`          | Combined project using all modules (end-to-end example) |
| `retriever/`        | Custom retrievers including self-query logic |
| `runnables/`        | Scripts to run chains or agents |
| `text-splitters/`   | Logic to chunk documents before embedding |
| `tool-binding/`     | Code to bind external tools to chains |
| `tools-toolkit/`    | Integration of toolkits for dynamic behavior |
| `vector-store/`     | Vector store management logic |
| `.env`              | Environment variables (OpenAI key, etc.) |
| `requirement.txt`   | Python dependencies for the entire project |

---

## 🧪 Getting Started

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/langchain-vector-projects.git
   cd langchain-vector-projects
   
2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows

4. **Install dependencies**
   ```bash
   pip install -r requirement.txt
