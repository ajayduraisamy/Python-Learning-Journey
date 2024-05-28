# 01_dataset_utils.py
# Synthetic dataset + helpers for Decision Tree visualization

import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split

def generate_dataset(n=400, random_state=42):
    np.random.seed(random_state)

    f1 = np.random.normal(5, 2, n)
    f2 = np.random.normal(10, 4, n)
    f3 = np.random.normal(20, 6, n)

    score = f1*0.2 + f2*0.3 + f3*0.1 + np.random.normal(0, 2, n)

    label = (score > np.median(score)).astype(int)

    df = pd.DataFrame({
        "f1": f1,
        "f2": f2,
        "f3": f3,
        "label": label
    })
    return df

def get_train_test(test_size=0.2):
    df = generate_dataset()
    X = df[["f1", "f2", "f3"]]
    y = df["label"]
    return train_test_split(X, y, test_size=test_size, random_state=42)

def save_output(path, fig=None):
    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    if fig is not None:
        fig.savefig(path)
