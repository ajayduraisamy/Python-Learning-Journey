import numpy as np

# Simple neuron demonstration

x = np.array([0.5, 1.0])
w = np.array([0.3, -0.7])
b = 0.1

z = np.dot(x, w) + b
output = 1 / (1 + np.exp(-z))  # sigmoid activation

print("Neuron output:", output)
