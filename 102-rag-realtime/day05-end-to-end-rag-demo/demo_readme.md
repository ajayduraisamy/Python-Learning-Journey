# End-to-End RAG Demo

## Overview
This module demonstrates a complete Retrieval Augmented Generation (RAG)
pipeline that integrates document ingestion, chunking, retrieval, and
answer generation into a single workflow.

---

## End-to-End Flow

1. Load documents
2. Split documents into chunks
3. Store chunks with embeddings
4. Retrieve top-K relevant chunks for a query
5. Generate an answer using retrieved context

---

## Why End-to-End RAG?
An end-to-end pipeline ensures that:
- Only relevant information is passed to the LLM
- Hallucinations are minimized
- The system scales to large document collections

---

## Real-World Use Cases
- Enterprise knowledge assistants
- Document-based chatbots
- Resume and policy question answering
