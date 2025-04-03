import numpy as np

np.random.seed(42)

fan_in = 100
fan_out = 50

# Xavier initialization
W_xavier = np.random.randn(fan_in, fan_out) * np.sqrt(1 / fan_in)

# He initialization (for ReLU)
W_he = np.random.randn(fan_in, fan_out) * np.sqrt(2 / fan_in)

x = np.random.randn(fan_in, 1)

out_xavier = W_xavier.T @ x
out_he = W_he.T @ x

print("Xavier -> mean:", out_xavier.mean(), "std:", out_xavier.std())
print("He -> mean:", out_he.mean(), "std:", out_he.std())
