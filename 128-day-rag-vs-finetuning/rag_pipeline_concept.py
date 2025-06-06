# Conceptual RAG pipeline (no framework)

pipeline = [
    "User query",
    "Embedding generation",
    "Vector database retrieval",
    "Relevant document chunks",
    "LLM with grounded context"
]

print("RAG Pipeline:")
for step in pipeline:
    print("-", step)
