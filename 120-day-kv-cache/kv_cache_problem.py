import numpy as np

np.random.seed(0)

seq_len = 6
dim = 4

# Simulate token-by-token generation without cache
X = np.random.randn(seq_len, dim)
Wq = np.random.randn(dim, dim)
Wk = np.random.randn(dim, dim)
Wv = np.random.randn(dim, dim)

for t in range(seq_len):
    Xt = X[:t+1]

    Q = Xt @ Wq
    K = Xt @ Wk
    V = Xt @ Wv

    scores = Q @ K.T
    print(f"Step {t}: recomputed K,V for {t+1} tokens")
