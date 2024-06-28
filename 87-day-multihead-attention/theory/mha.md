# Multi-Head Attention (MHA)

### Why multiple heads?
A single attention head focuses on ONE type of relationship.

Multi-head attention:
- Splits Q/K/V into multiple subspaces
- Each head learns different patterns
- Results are concatenated
- Output = richer representation

---

## Steps:
1. Linear projections -> Q, K, V
2. Split into h heads
3. Apply scaled dot-product attention per head
4. Concatenate results
5. Apply final linear layer

This is the heart of all Transformers.
