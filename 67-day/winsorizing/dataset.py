import numpy as np
import pandas as pd

def load_data():
    np.random.seed(42)
    data = np.concatenate([
        np.random.normal(70, 12, 500),
        np.array([150, 160, 200])
    ])
    return pd.DataFrame({"value": data})
