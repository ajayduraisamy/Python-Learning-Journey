# 01_dataset.py
# Synthetic dataset for SVM classification:
# Predict whether a person is "Fit" or "Unfit" based on:
# - workout_hours_per_week
# - daily_calorie_intake

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def generate_dataset(n=350, random_state=42):
    np.random.seed(random_state)

    workout = np.random.uniform(0, 14, n)
    calories = np.random.uniform(1500, 4000, n)

    # simple health score formula
    score = (
        0.5 * workout -
        0.002 * calories +
        np.random.normal(0, 0.5, n)
    )

    fit = (score > -1).astype(int)

    df = pd.DataFrame({
        "workout": workout,
        "calories": calories,
        "fit": fit
    })

    return df

def get_train_test(test_size=0.2):
    df = generate_dataset()
    X = df[["workout", "calories"]]
    y = df["fit"]
    return train_test_split(X, y, test_size=test_size, random_state=42, stratify=y)
