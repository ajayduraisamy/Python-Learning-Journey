# Attention Mechanism — Q, K, V Basics

Attention decides:
"Which parts of the input should I focus on?"

---

## 1️⃣ Query (Q)
The thing asking the question.

## 2️⃣ Key (K)
Possible matches.

## 3️⃣ Value (V)
Information to return if match is strong.

---

## ⚡ Scaled Dot-Product Attention

Formula:
    Attention(Q,K,V) = softmax(QKᵀ / √d_k) * V

Step-by-step:
1. Compute similarity between Q and K → QKᵀ
2. Scale by sqrt(depth) to avoid large gradients
3. Apply softmax → attention weights
4. Weighted sum with V → output

---

This is the core of:
- Transformers
- GPT
- BERT
- Vision Transformers
