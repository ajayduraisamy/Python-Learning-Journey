# 01_dataset.py
# Synthetic dataset for KNN classification:
# Predict if a student will pass based on hours studied and test anxiety level.

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def generate_dataset(n=300, random_state=42):
    np.random.seed(random_state)

    hours_study = np.random.uniform(0, 10, n)
    anxiety = np.random.uniform(1, 10, n)

    score = (
        0.7 * hours_study -
        0.5 * anxiety +
        np.random.normal(0, 1, n)
    )

    passed = (score > 2).astype(int)

    df = pd.DataFrame({
        "hours_study": hours_study,
        "anxiety": anxiety,
        "passed": passed
    })

    return df

def get_train_test(test_size=0.2):
    df = generate_dataset()
    X = df[["hours_study", "anxiety"]]
    y = df["passed"]
    return train_test_split(X, y, test_size=test_size, random_state=42, stratify=y)
