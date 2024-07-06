# Temperature, Top-K, Top-P Sampling

## Temperature (T)
Controls randomness:
- T < 1 → sharper, more confident
- T > 1 → more random

logits = logits / T

---

## Top-K Sampling
Pick next token from top K most likely tokens.

---

## Top-P (Nucleus) Sampling
Pick smallest set of tokens whose cumulative probability ≥ P.
Example:
- P=0.9 → use only tokens that together form 90% probability mass.

---

These methods make generation:
- More natural
- Less repetitive
- More controllable
