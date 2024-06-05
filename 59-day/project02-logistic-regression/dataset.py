import numpy as np
import pandas as pd

def load_data(n=300):
    np.random.seed(42)
    hours = np.random.uniform(0, 10, n)
    passed = (hours + np.random.randn(n) > 5).astype(int)
    return pd.DataFrame({"hours": hours, "passed": passed})
