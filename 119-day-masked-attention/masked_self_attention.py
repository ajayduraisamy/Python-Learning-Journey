import numpy as np

np.random.seed(0)

# Token embeddings
X = np.random.randn(4, 6)

# Weight matrices
Wq = np.random.randn(6, 6)
Wk = np.random.randn(6, 6)
Wv = np.random.randn(6, 6)

Q = X @ Wq
K = X @ Wk
V = X @ Wv

dk = Q.shape[-1]

# Attention scores
scores = Q @ K.T / np.sqrt(dk)

# Apply causal mask
mask = np.triu(np.ones_like(scores), k=1) * -1e9
masked_scores = scores + mask

# Softmax
weights = np.exp(masked_scores) / np.sum(
    np.exp(masked_scores), axis=1, keepdims=True
)

output = weights @ V

print("Masked attention weights:\n", weights)
print("Output:\n", output)
