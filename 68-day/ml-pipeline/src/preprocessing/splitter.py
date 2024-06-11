# splitter.py
# Train/Val/Test split with stratification

import pandas as pd
from sklearn.model_selection import train_test_split
from utils.logger import log

def split_dataset(df):
    log("Splitting dataset into train/val/test...")

    X = df.drop("Class", axis=1)
    y = df["Class"]

    # 70% train, 15% val, 15% test
    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=0.30, random_state=42, stratify=y
    )

    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=0.50, random_state=42, stratify=y_temp
    )

    log(f"Train: {len(X_train)}, Val: {len(X_val)}, Test: {len(X_test)}")

    return X_train, X_val, X_test, y_train, y_val, y_test
