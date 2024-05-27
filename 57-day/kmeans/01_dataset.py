import numpy as np
import pandas as pd

def generate_kmeans_dataset(n=400, random_state=42):
    np.random.seed(random_state)
    c1 = np.random.normal(loc=[2, 2], scale=0.7, size=(n//3, 2))
    c2 = np.random.normal(loc=[7, 7], scale=0.7, size=(n//3, 2))
    c3 = np.random.normal(loc=[2, 8], scale=0.7, size=(n//3, 2))
    data = np.vstack([c1, c2, c3])
    df = pd.DataFrame(data, columns=["x", "y"])
    return df
