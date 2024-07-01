# Full Transformer Architecture (Encoder + Decoder)

### Components:
1) Embedding + Positional Encoding
2) N-layer Encoder Stack
3) N-layer Decoder Stack
4) Linear projection to vocabulary

Encoder:
- Multi-Head Self-Attention
- Feed Forward
- Residual + LayerNorm

Decoder:
- Masked Self-Attention
- Encoder-Decoder Attention
- Feed Forward
- Residual + LayerNorm

Transformers power:
- T5, BART, mT5
- Neural Machine Translation
- Pegasus
