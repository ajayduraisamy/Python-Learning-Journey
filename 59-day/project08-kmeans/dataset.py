import numpy as np
import pandas as pd

def load_data(n=300):
    np.random.seed(42)
    c1 = np.random.normal(0, 1, (n//3, 2))
    c2 = np.random.normal(5, 1, (n//3, 2))
    c3 = np.random.normal(10, 1, (n//3, 2))
    data = np.vstack([c1, c2, c3])
    return pd.DataFrame(data, columns=["x","y"])
