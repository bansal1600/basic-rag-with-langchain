from langchain_community.retrievers import WikipediaRetriever

retriver = WikipediaRetriever(
    top_k_results=2,
    lang="en",
)

query = "What is the capital of France?"

results = retriver.invoke(query)
print("Top result:", results)  # Output: "The capital of France is Paris."