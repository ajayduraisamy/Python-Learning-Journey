# Document Ingestion and Chunking – RAG

## What is Document Ingestion?
Document ingestion is the process of loading raw documents such as
text files, PDFs, or web content and preparing them for retrieval.

In RAG systems, documents are not used directly.
They are cleaned, split into chunks, and converted into embeddings.

---

## Why Chunking is Required
Large documents exceed the context length of LLMs.
Chunking ensures:
- Better retrieval accuracy
- Lower token usage
- Reduced noise in responses

---

## Chunking Strategies

### 1. Fixed Size Chunking
Documents are split into chunks of equal length.

### 2. Overlapping Chunking
Small overlap between chunks prevents loss of context.

### 3. Semantic Chunking
Splits text based on sentences or meaning.

---

## Best Practices
- Chunk size: 300–500 tokens
- Overlap: 30–50 tokens
- Preserve metadata (source, page number)
