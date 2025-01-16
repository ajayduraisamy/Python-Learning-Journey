# ------------------------------------
# RETRIEVAL PIPELINE (TOP-K SEARCH)
# ------------------------------------

import math

# Step 1: Document embeddings (simulated)
documents = {
    "doc1": ("RAG improves LLM accuracy by retrieval.", [0.1, 0.2, 0.9]),
    "doc2": ("Vector databases store embeddings.", [0.8, 0.1, 0.2]),
    "doc3": ("Chunking improves retrieval precision.", [0.2, 0.9, 0.1]),
    "doc4": ("LLMs hallucinate without context.", [0.15, 0.25, 0.85])
}

# Step 2: Query embedding
query_embedding = [0.1, 0.3, 0.8]

# Step 3: Cosine similarity
def cosine_similarity(v1, v2):
    dot = sum(a*b for a, b in zip(v1, v2))
    mag1 = math.sqrt(sum(a*a for a in v1))
    mag2 = math.sqrt(sum(b*b for b in v2))
    return dot / (mag1 * mag2)

# Step 4: Similarity search
scores = []
for doc_id, (text, embedding) in documents.items():
    score = cosine_similarity(query_embedding, embedding)
    scores.append((doc_id, text, score))

# Step 5: Sort by similarity (descending)
scores.sort(key=lambda x: x[2], reverse=True)

# Step 6: Top-K retrieval
TOP_K = 2
top_k_docs = scores[:TOP_K]

# Output
print("Top-K Retrieved Documents:\n")
for doc_id, text, score in top_k_docs:
    print(f"{doc_id} | Score: {score:.3f}")
    print(text)
    print()
