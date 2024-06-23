# Advanced Activation Functions — Swish, Mish, GELU

### 1. Swish
Formula: x * sigmoid(x)
- Used in EfficientNet
- Smooth and avoids dead neurons

### 2. GELU
Formula: x * Φ(x)
- Used in Transformers (BERT, GPT)
- Smooth like Swish but probabilistic

### 3. Mish
Formula: x * tanh(softplus(x))
- Sometimes better than ReLU
