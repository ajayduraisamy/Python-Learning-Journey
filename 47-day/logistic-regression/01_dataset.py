# 01_dataset.py
# Synthetic dataset: Student pass/fail classification

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def generate_dataset(n=300, random_state=42):
    np.random.seed(random_state)

    hours_study = np.random.uniform(0, 10, n)
    hours_sleep = np.random.uniform(4, 10, n)
    prev_score = np.random.uniform(0, 100, n)

    # Passing probability formula
    prob = (
        0.4 * hours_study +
        0.2 * (hours_sleep - 5) +
        0.3 * (prev_score / 100) +
        np.random.normal(0, 0.2, n)
    )

    prob = 1 / (1 + np.exp(-prob))  # sigmoid
    passed = (prob >= 0.5).astype(int)

    df = pd.DataFrame({
        "hours_study": hours_study,
        "hours_sleep": hours_sleep,
        "prev_score": prev_score,
        "passed": passed
    })

    return df

def get_train_test(test_size=0.2):
    df = generate_dataset()
    X = df[["hours_study", "hours_sleep", "prev_score"]]
    y = df["passed"]
    return train_test_split(X, y, test_size=test_size, random_state=42, stratify=y)
