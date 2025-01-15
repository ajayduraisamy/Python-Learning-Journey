# Retrieval Augmented Generation (RAG) – Overview

Retrieval Augmented Generation (RAG) is an AI architecture that combines
information retrieval techniques with Large Language Models (LLMs) to
produce more accurate, reliable, and up-to-date responses.

Traditional LLMs generate answers only from their training data.
RAG enhances this by retrieving relevant external documents in real time
and injecting them into the model’s context before generating a response.

---

## Why RAG is Needed

Large Language Models have several limitations:
- Knowledge is static and frozen at training time
- Cannot access private or organization-specific data
- High chance of hallucinations
- Poor performance on domain-specific queries

RAG addresses these limitations by grounding responses in retrieved data.

---

## Core Idea of RAG

Instead of asking the LLM directly:

User → LLM → Answer

RAG follows this approach:

User → Retrieve Relevant Data → LLM → Answer

This makes responses more factual and trustworthy.

---

## Key Components of RAG

1. User Query  
The question or prompt provided by the user.

2. Embedding Model  
Converts text into numerical vectors that capture semantic meaning.

3. Vector Database  
Stores document embeddings and enables similarity search.

4. Retriever  
Fetches the most relevant document chunks based on the query.

5. Language Model  
Generates the final response using retrieved context.

---

## Simple Example

Question:
"What is the company refund policy?"

Without RAG:
The model may guess or hallucinate an answer.

With RAG:
The system retrieves the refund policy document and generates
an accurate answer based on real data.

---

## Advantages of RAG

- Reduces hallucinations
- Uses real-time or private data
- Improves factual accuracy
- Suitable for enterprise applications

---

## Common Use Cases

- AI chatbots
- Enterprise knowledge base
- Resume and document question answering
- Legal and medical assistants
