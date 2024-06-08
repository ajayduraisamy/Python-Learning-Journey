import numpy as np
import pandas as pd

def load_data():
    np.random.seed(42)
    data = np.concatenate([
        np.random.normal(100, 15, 500),
        np.array([200, 220, 250])
    ])
    return pd.DataFrame({"value": data})
