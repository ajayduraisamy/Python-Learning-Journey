import numpy as np
import pandas as pd

def load_data():
    np.random.seed(42)
    # Skewed distribution
    data = np.random.exponential(scale=50, size=500)
    return pd.DataFrame({"value": data})
