import numpy as np
import pandas as pd

def load_data(n=300):
    np.random.seed(42)
    x1 = np.random.randn(n)
    x2 = x1*0.8 + np.random.randn(n)*0.2
    x3 = x1*0.5 + np.random.randn(n)*0.2
    return pd.DataFrame({"x1":x1,"x2":x2,"x3":x3})
