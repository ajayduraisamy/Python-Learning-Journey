import numpy as np

np.random.seed(42)

layers = 20
x = np.random.randn(1)

for i in range(layers):
    w = np.random.randn() * 2.0  # large weights
    x = w * x

print("Output after many layers:", x)
