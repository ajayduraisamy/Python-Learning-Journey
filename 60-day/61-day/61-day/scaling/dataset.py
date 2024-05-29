import numpy as np
import pandas as pd

def load_data(n=300):
    np.random.seed(42)
    x1 = np.random.normal(50, 10, n)
    x2 = np.random.uniform(0, 1, n)
    x3 = np.random.normal(100, 50, n)
    return pd.DataFrame({"x1": x1, "x2": x2, "x3": x3})
