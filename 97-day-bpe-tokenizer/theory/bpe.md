# Byte Pair Encoding (BPE)

Why BPE?
- Word-level → OOV problem
- Char-level → long sequences
- BPE → best of both

How it works:
1) Start with characters
2) Count most frequent adjacent pairs
3) Merge the most frequent pair
4) Repeat until vocab size reached

Used by:
- GPT-2 / GPT-3
- RoBERTa
- LLaMA (variant)
