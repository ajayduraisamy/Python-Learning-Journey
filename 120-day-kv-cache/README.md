# Day 120 – KV Cache in Transformer Inference

KV Cache is a critical optimization used during
autoregressive inference in large language models.

Covered:
- Why naive attention recomputes keys and values
- Time complexity without caching
- How KV cache reuses past keys and values
- Why KV cache is used only during inference

KV cache is essential for fast LLM decoding.
