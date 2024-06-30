# Transformer Decoder Block (GPT Style)

Decoder consists of:

1️⃣ Masked Multi-Head Self-Attention  
   - Ensures token i sees only tokens <= i  
   - Required for autoregressive models (GPT)

2️⃣ (Optional) Encoder-Decoder Attention  
   - Not used in GPT  
   - Used in T5, BART, original Transformer

3️⃣ Feed Forward Network (FFN)

4️⃣ Residual + LayerNorm

---

## Masking
To prevent cheating (looking ahead):
Mask future positions with -inf so softmax → 0.
