from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()
results = search_tool.invoke("What is the capital of France?")
print(results)  # Output: "The capital of France is Paris."