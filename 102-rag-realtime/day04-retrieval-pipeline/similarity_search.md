# Retrieval Pipeline and Similarity Search – RAG

## What is Retrieval in RAG?
Retrieval is the process of finding the most relevant document chunks
for a given user query.

Instead of passing the entire document to the LLM, only the most
relevant chunks are selected.

---

## Retrieval Pipeline Steps

1. User provides a query
2. Query is converted into an embedding
3. Similarity search is performed against stored document embeddings
4. Top-K most relevant chunks are selected
5. Selected chunks are passed to the LLM as context

---

## What is Top-K Search?
Top-K search returns the K most similar documents.
Common values of K are 3 to 10.

Higher K:
- More context
- Higher token cost

Lower K:
- Faster
- Less noise

---

## Why Retrieval is Important
- Improves answer accuracy
- Reduces hallucination
- Keeps context focused
- Makes system scalable
