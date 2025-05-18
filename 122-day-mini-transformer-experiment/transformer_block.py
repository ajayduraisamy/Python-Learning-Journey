import numpy as np

def softmax(x):
    exp = np.exp(x - np.max(x))
    return exp / exp.sum(axis=-1, keepdims=True)

def self_attention(X):
    dim = X.shape[-1]
    Wq = np.random.randn(dim, dim)
    Wk = np.random.randn(dim, dim)
    Wv = np.random.randn(dim, dim)

    Q = X @ Wq
    K = X @ Wk
    V = X @ Wv

    scores = Q @ K.T / np.sqrt(dim)
    weights = softmax(scores)
    return weights @ V

# Token embeddings (3 tokens)
X = np.random.randn(3, 6)

out = self_attention(X)
print("Transformer block output:\n", out)
