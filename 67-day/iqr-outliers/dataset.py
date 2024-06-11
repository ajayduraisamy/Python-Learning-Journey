import pandas as pd
import numpy as np

def load_data():
    np.random.seed(42)
    # Normal distribution + some outliers
    data = np.concatenate([np.random.normal(50, 10, 400), np.array([120, 130, 150])])
    df = pd.DataFrame({"value": data})
    return df
