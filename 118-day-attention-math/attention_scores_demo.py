import numpy as np

# Example Query, Keys
query = np.array([1.0, 0.0, 1.0])
keys = np.array([
    [1.0, 1.0, 0.0],
    [0.0, 1.0, 1.0],
    [1.0, 0.0, 1.0]
])

# Dot-product attention scores
scores = np.dot(keys, query)

# Softmax
exp_scores = np.exp(scores)
attention_weights = exp_scores / np.sum(exp_scores)

print("Attention scores:", scores)
print("Attention weights:", attention_weights)
