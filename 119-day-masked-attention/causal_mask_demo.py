import numpy as np

seq_len = 5

# Create causal mask
mask = np.triu(np.ones((seq_len, seq_len)), k=1) * -1e9

print("Causal mask:\n", mask)
