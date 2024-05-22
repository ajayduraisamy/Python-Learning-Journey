# 01_dataset_utils.py
# Dataset + utilities in single file

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import os

def generate_dataset(n=350, random_state=42):
    np.random.seed(random_state)

    happy = np.random.randint(0, 10, n)
    sad = np.random.randint(0, 10, n)

    score = happy - sad + np.random.normal(0, 1, n)
    sentiment = (score > 0).astype(int)

    df = pd.DataFrame({
        "happy": happy,
        "sad": sad,
        "sentiment": sentiment
    })
    return df

def get_train_test(test_size=0.2):
    df = generate_dataset()
    X = df[["happy", "sad"]]
    y = df["sentiment"]
    return train_test_split(X, y, test_size=test_size, random_state=42, stratify=y)

def save_metrics(path, text):
    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    with open(path, "w") as f:
        f.write(text)
