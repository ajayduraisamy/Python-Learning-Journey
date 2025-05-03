import numpy as np

np.random.seed(42)

# Token embeddings (3 tokens, dim=4)
X = np.random.randn(3, 4)

# Weight matrices
Wq = np.random.randn(4, 4)
Wk = np.random.randn(4, 4)
Wv = np.random.randn(4, 4)

Q = X @ Wq
K = X @ Wk
V = X @ Wv

# Scaled dot-product attention
dk = Q.shape[-1]
scores = Q @ K.T / np.sqrt(dk)

weights = np.exp(scores) / np.sum(np.exp(scores), axis=1, keepdims=True)
output = weights @ V

print("Attention weights:\n", weights)
print("Attention output:\n", output)
