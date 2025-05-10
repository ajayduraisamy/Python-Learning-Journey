import numpy as np

np.random.seed(0)

seq_len = 6
dim = 4

X = np.random.randn(seq_len, dim)
Wq = np.random.randn(dim, dim)
Wk = np.random.randn(dim, dim)
Wv = np.random.randn(dim, dim)

K_cache = []
V_cache = []

for t in range(seq_len):
    xt = X[t:t+1]

    q = xt @ Wq
    k = xt @ Wk
    v = xt @ Wv

    K_cache.append(k)
    V_cache.append(v)

    K = np.vstack(K_cache)
    V = np.vstack(V_cache)

    scores = q @ K.T
    print(f"Step {t}: reused cached K,V (size={len(K_cache)})")
