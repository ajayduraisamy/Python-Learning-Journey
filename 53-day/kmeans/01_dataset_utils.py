# 01_dataset_utils.py
# Synthetic dataset + utilities for K-Means clustering

import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split

def generate_dataset(n=400, random_state=42):
    np.random.seed(random_state)

    # Create 3 natural clusters
    c1 = np.random.normal(loc=[2, 2], scale=0.5, size=(n//3, 2))
    c2 = np.random.normal(loc=[6, 6], scale=0.5, size=(n//3, 2))
    c3 = np.random.normal(loc=[10, 2], scale=0.5, size=(n//3, 2))

    data = np.vstack([c1, c2, c3])
    df = pd.DataFrame(data, columns=["x", "y"])
    return df

def get_data():
    df = generate_dataset()
    X = df[["x", "y"]]
    return X

def save_metrics(path, text):
    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    with open(path, "w") as f:
        f.write(text)
