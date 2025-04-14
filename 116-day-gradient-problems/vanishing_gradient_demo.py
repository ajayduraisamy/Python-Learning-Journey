import numpy as np

np.random.seed(42)

layers = 20
x = np.random.randn(1)

for i in range(layers):
    w = np.random.randn() * 0.1  # small weights
    x = np.tanh(w * x)

print("Output after many layers:", x)
