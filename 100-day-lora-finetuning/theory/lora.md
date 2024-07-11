# LoRA — Low Rank Adaptation

Idea:
W_new = W_frozen + A × B

Where:
- W_frozen → pretrained weights (frozen)
- A, B → small trainable matrices
- rank r << d

Benefits:
- Train only ~1–5% parameters
- Much faster
- Much cheaper
- Same quality

Used by:
- OpenAI
- HuggingFace PEFT
- LLaMA fine-tuning
