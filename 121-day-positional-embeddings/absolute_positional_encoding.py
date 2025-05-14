import numpy as np

def positional_encoding(seq_len, dim):
    pe = np.zeros((seq_len, dim))
    for pos in range(seq_len):
        for i in range(0, dim, 2):
            pe[pos, i] = np.sin(pos / (10000 ** (i / dim)))
            pe[pos, i + 1] = np.cos(pos / (10000 ** (i / dim)))
    return pe

pe = positional_encoding(seq_len=5, dim=6)
print("Absolute positional encodings:\n", pe)
