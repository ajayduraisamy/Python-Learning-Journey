# FlashAttention — Fast & Memory Efficient Attention

Problem with standard attention:
- Stores full QKᵀ matrix (O(n²) memory)
- Very slow for long sequences

FlashAttention idea:
- Compute attention in BLOCKS (tiles)
- Never materialize full attention matrix
- Use streaming softmax
- Much lower memory footprint

Used in:
- GPT-4
- LLaMA
- Mistral
- Falcon
