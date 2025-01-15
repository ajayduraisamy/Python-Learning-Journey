# ---------------------------------------
# BASIC EMBEDDINGS + VECTOR SEARCH DEMO
# ---------------------------------------

import math

# Step 1: Fake embeddings (for learning)
documents = {
    "doc1": [0.1, 0.2, 0.9],
    "doc2": [0.8, 0.1, 0.2],
    "doc3": [0.2, 0.9, 0.1]
}

query_embedding = [0.1, 0.3, 0.8]

# Step 2: Cosine similarity function
def cosine_similarity(v1, v2):
    dot = sum(a*b for a, b in zip(v1, v2))
    mag1 = math.sqrt(sum(a*a for a in v1))
    mag2 = math.sqrt(sum(b*b for b in v2))
    return dot / (mag1 * mag2)

# Step 3: Similarity search
scores = {}
for doc, embedding in documents.items():
    score = cosine_similarity(query_embedding, embedding)
    scores[doc] = score

# Step 4: Get most similar document
best_match = max(scores, key=scores.get)

print("Query Embedding:", query_embedding)
print("Similarity Scores:", scores)
print("Most Relevant Document:", best_match)
print("Similarity Score:", scores[best_match])