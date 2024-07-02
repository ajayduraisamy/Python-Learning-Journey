# GPT Architecture (Decoder-Only Transformer)

GPT is built from:
- Stacked decoder blocks
- Masked self-attention
- No encoder
- Predicts next token (auto-regressive LM)

Key concepts:
1) Mask future tokens (look-ahead mask)
2) Use only decoder block from Transformer
3) LM head: linear projection to vocab size
4) Autoregressive generation: feed output token back in

GPT-2, GPT-3, GPT-4 all follow this core principle.
