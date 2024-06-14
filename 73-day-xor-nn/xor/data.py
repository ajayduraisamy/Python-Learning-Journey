import numpy as np

def load_xor():
    # XOR truth table
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])
    y = np.array([[0], [1], [1], [0]])
    return X, y
