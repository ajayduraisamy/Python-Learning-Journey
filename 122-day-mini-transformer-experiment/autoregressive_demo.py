import numpy as np

def causal_mask(n):
    return np.triu(np.ones((n, n)), k=1) * -1e9

def softmax(x):
    exp = np.exp(x - np.max(x))
    return exp / exp.sum(axis=-1, keepdims=True)

np.random.seed(0)

seq_len = 4
dim = 6
X = np.random.randn(seq_len, dim)

Wq = np.random.randn(dim, dim)
Wk = np.random.randn(dim, dim)
Wv = np.random.randn(dim, dim)

Q = X @ Wq
K = X @ Wk
V = X @ Wv

scores = Q @ K.T / np.sqrt(dim)
scores += causal_mask(seq_len)

weights = softmax(scores)
output = weights @ V

print("Causal attention weights:\n", weights)
print("Autoregressive output:\n", output)
