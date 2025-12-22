# 01_data.py
# Load Iris dataset and provide train/test split

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd

def load_dataset(as_frame=True):
    data = load_iris(as_frame=as_frame)
    X = data.data
    y = data.target
    feature_names = data.feature_names
    target_names = data.target_names
    return X, y, feature_names, target_names

def get_train_test(test_size=0.2, random_state=42):
    X, y, _, _ = load_dataset()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    return X_train, X_test, y_train, y_test
