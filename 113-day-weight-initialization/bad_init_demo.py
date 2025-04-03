import numpy as np

np.random.seed(42)

# Naive initialization
W = np.random.randn(100, 100) * 10  # too large
x = np.random.randn(100, 1)

# Forward pass
out = W @ x

print("Mean:", out.mean())
print("Std Dev:", out.std())
