# 01_dataset_utils.py
# Dataset + utility functions

import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split

def generate_dataset(n=300, random_state=42):
    np.random.seed(random_state)

    # Two clusters separable by a line
    x1 = np.random.normal(2, 1, (n//2, 2))
    x2 = np.random.normal(6, 1, (n//2, 2))

    X = np.vstack([x1, x2])
    y = np.array([0]*(n//2) + [1]*(n//2))

    df = pd.DataFrame(X, columns=["f1", "f2"])
    df["label"] = y

    return df

def get_train_test(test_size=0.2):
    df = generate_dataset()
    X = df[["f1", "f2"]]
    y = df["label"]
    return train_test_split(X, y, test_size=test_size, random_state=42, stratify=y)

def save_image(path, fig):
    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    fig.savefig(path)
