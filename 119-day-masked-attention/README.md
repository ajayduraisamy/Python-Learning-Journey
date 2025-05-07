# Day 119 – Masked Self-Attention (Causal Attention)

Masked self-attention prevents a token from attending
to future tokens during training and inference.

Covered:
- Why masking is required for autoregressive models
- Causal (look-ahead) masks
- Difference between encoder and decoder attention
- How masking enforces left-to-right generation

This is a core concept behind GPT-style models.
