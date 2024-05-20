# 01_dataset.py
# Synthetic dataset for Random Forest Classification:
# Predict if a patient is at high risk based on:
# - cholesterol
# - blood_pressure
# - age

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def generate_dataset(n=400, random_state=42):
    np.random.seed(random_state)

    age = np.random.randint(20, 80, n)
    cholesterol = np.random.randint(150, 300, n)
    bp = np.random.randint(90, 180, n)

    score = (
        0.02 * age +
        0.015 * cholesterol +
        0.03 * bp +
        np.random.normal(0, 3, n)
    )

    high_risk = (score > 20).astype(int)

    df = pd.DataFrame({
        "age": age,
        "cholesterol": cholesterol,
        "blood_pressure": bp,
        "high_risk": high_risk
    })

    return df

def get_train_test(test_size=0.2):
    df = generate_dataset()
    X = df[["age", "cholesterol", "blood_pressure"]]
    y = df["high_risk"]
    return train_test_split(X, y, test_size=test_size, random_state=42, stratify=y)
