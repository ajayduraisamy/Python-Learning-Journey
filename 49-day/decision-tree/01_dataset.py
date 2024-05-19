# 01_dataset.py
# Synthetic dataset for decision tree classification:
# Predict if a customer will buy a product based on:
# - age
# - income
# - browsing time

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def generate_dataset(n=300, random_state=42):
    np.random.seed(random_state)

    age = np.random.randint(18, 60, n)
    income = np.random.randint(20000, 150000, n)
    browse_time = np.random.uniform(0, 40, n)

    score = (
        0.015 * age +
        0.0001 * income +
        0.1 * browse_time +
        np.random.normal(0, 3, n)
    )

    bought = (score > 8).astype(int)

    df = pd.DataFrame({
        "age": age,
        "income": income,
        "browse_time": browse_time,
        "bought": bought
    })

    return df

def get_train_test(test_size=0.2):
    df = generate_dataset()
    X = df[["age", "income", "browse_time"]]
    y = df["bought"]
    return train_test_split(X, y, test_size=test_size, random_state=42, stratify=y)
