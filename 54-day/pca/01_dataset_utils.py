# 01_dataset_utils.py
# Dataset + Utilities for PCA

import numpy as np
import pandas as pd
import os

def generate_dataset(n=500, random_state=42):
    np.random.seed(random_state)

    # Create 3 highly correlated features
    x1 = np.random.normal(0, 1, n)
    x2 = x1 * 0.8 + np.random.normal(0, 0.2, n)   # correlated with x1
    x3 = x1 * 0.5 + x2 * 0.3 + np.random.normal(0, 0.1, n)

    df = pd.DataFrame({
        "feature1": x1,
        "feature2": x2,
        "feature3": x3
    })
    return df

def get_data():
    return generate_dataset()

def save_output(path, text):
    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    with open(path, "w") as f:
        f.write(text)
