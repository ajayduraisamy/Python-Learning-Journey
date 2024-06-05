import numpy as np
import pandas as pd

def load_data(n=100):
    np.random.seed(42)
    x = np.random.normal(50, 10, n)
    x[5] = 150   # add outliers
    x[25] = -30
    return pd.DataFrame({"x": x})
