# 01_dataset_utils.py
# Synthetic dataset + utilities for Neural Network (MLPClassifier)

import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split

def generate_dataset(n=400, random_state=42):
    np.random.seed(random_state)

    # Logical XOR-like dataset (NN friendly)
    x1 = np.random.randint(0, 2, n)
    x2 = np.random.randint(0, 2, n)

    label = (x1 ^ x2).astype(int)  # XOR output

    df = pd.DataFrame({
        "x1": x1,
        "x2": x2,
        "label": label
    })
    return df

def get_train_test(test_size=0.2):
    df = generate_dataset()
    X = df[["x1", "x2"]]
    y = df["label"]
    return train_test_split(X, y, test_size=test_size, random_state=42, stratify=y)

def save_output(path, text):
    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    with open(path, "w") as f:
        f.write(text)
