# Integrating RoPE into GPT

Changes from GPT-mini:
- Remove sinusoidal positional embeddings
- Apply RoPE directly to Q & K
- Attention becomes position-aware by rotation

This is used in:
- LLaMA
- Mistral
- GPT-NeoX

RoPE improves:
- Long context handling
- Relative position understanding
