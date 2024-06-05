import numpy as np
import pandas as pd

def load_data(n=200, random_state=42):
    np.random.seed(random_state)
    x = np.random.rand(n) * 10
    y = 3*x + 5 + np.random.randn(n)
    return pd.DataFrame({"x": x, "y": y})
