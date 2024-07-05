# Rotary Positional Embeddings (RoPE)

RoPE encodes position by rotating Q & K vectors instead of adding embeddings.

Advantages:
- Relative position awareness
- Better extrapolation to long sequences
- Used in LLaMA, GPT-NeoX, Falcon

Rotation:
[x1, x2] → [x1*cosθ - x2*sinθ, x1*sinθ + x2*cosθ]

Applied only to:
- Query (Q)
- Key (K)

Not applied to:
- Value (V)
