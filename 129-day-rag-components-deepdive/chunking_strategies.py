# Demonstration of chunking strategies

text = "RAG systems depend heavily on chunking strategy for retrieval quality."

# Fixed-size chunking
fixed_chunks = [text[i:i+20] for i in range(0, len(text), 20)]

# Semantic-style chunking (simplified)
semantic_chunks = [
    "RAG systems depend heavily",
    "on chunking strategy",
    "for retrieval quality"
]

print("Fixed chunks:")
for c in fixed_chunks:
    print("-", c)

print("\nSemantic chunks:")
for c in semantic_chunks:
    print("-", c)
