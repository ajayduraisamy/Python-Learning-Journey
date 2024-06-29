# Transformer Encoder Block

An encoder block contains:

1️⃣ **Multi-Head Attention**  
2️⃣ **Add & LayerNorm**  
3️⃣ **Feed-Forward Network (FFN)**  
4️⃣ **Add & LayerNorm**  

---

## FFN Formula:
FFN(x) = ReLU(xW1 + b1)W2 + b2

---

## Why Residual Connections?
Helps gradients flow, prevents vanishing.

---

## Why LayerNorm?
Stabilizes training, normalizes features per token.

This block is repeated N times in:
- BERT
- ViT
- Transformers Encoder
