# Embeddings and Vector Databases – RAG

## What are Embeddings?
Embeddings are numerical vector representations of text that capture
semantic meaning. Similar texts produce vectors that are close to each
other in vector space.

Example:
"I like AI" and "I love artificial intelligence"
→ embeddings are very similar.

---

## Why Embeddings are Important in RAG
Keyword search fails when words differ.
Embeddings enable semantic search, meaning the system understands
intent rather than exact words.

---

## Vector Database
A vector database stores embeddings and allows fast similarity search.
Instead of searching text, it searches vectors.

Popular vector databases:
- FAISS
- Chroma
- Pinecone
- Weaviate

---

## Similarity Search
Common methods:
- Cosine similarity (most used)
- Euclidean distance
- Dot product

The retriever returns the Top-K most similar documents.
