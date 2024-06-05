import numpy as np
import pandas as pd

def load_data(n=300):
    np.random.seed(42)
    x1 = np.random.randint(0,2,n)
    x2 = np.random.randint(0,2,n)
    y = (x1 ^ x2).astype(int)
    return pd.DataFrame({"x1":x1,"x2":x2,"label":y})
