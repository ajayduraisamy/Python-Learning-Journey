import numpy as np
import pandas as pd

def load_data():
    np.random.seed(42)
    x = np.random.normal(10, 2, 20)
    x[3] = np.nan
    x[7] = np.nan
    x[12] = np.nan
    return pd.DataFrame({"x": x})
