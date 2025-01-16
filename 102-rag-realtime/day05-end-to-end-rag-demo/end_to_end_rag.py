# -----------------------------------------
# END-TO-END RAG PIPELINE (CONCEPT DEMO)
# -----------------------------------------

import math

# Step 1: Load document
with open("knowledge_base.txt", "r") as file:
    document = file.read()

# Step 2: Chunking
def chunk_text(text, chunk_size=20):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i + chunk_size]))
    return chunks

chunks = chunk_text(document)

# Step 3: Fake embeddings generator
def fake_embedding(text):
    return [len(text) % 10, sum(ord(c) for c in text) % 10, len(text.split()) % 10]

# Create embeddings
chunk_embeddings = [(chunk, fake_embedding(chunk)) for chunk in chunks]

# Step 4: Cosine similarity
def cosine_similarity(v1, v2):
    dot = sum(a*b for a, b in zip(v1, v2))
    mag1 = math.sqrt(sum(a*a for a in v1))
    mag2 = math.sqrt(sum(b*b for b in v2))
    return dot / (mag1 * mag2)

# Step 5: Retrieve Top-K chunks
def retrieve_chunks(query, k=2):
    query_embedding = fake_embedding(query)
    scores = []
    for chunk, emb in chunk_embeddings:
        score = cosine_similarity(query_embedding, emb)
        scores.append((chunk, score))
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:k]

# Step 6: Generate answer (LLM simulation)
def generate_answer(query, retrieved_chunks):
    answer = "Answer based on retrieved context:\n"
    for chunk, score in retrieved_chunks:
        answer += f"- {chunk}\n"
    return answer

# Step 7: Realtime interaction
while True:
    query = input("\nAsk a question (type 'exit' to quit): ")
    if query.lower() == "exit":
        print("Exiting RAG system.")
        break

    retrieved = retrieve_chunks(query)
    response = generate_answer(query, retrieved)
    print("\n", response)
    print("Similarity scores:", [f"{chunk}: {score:.4f}" for chunk, score in retrieved])