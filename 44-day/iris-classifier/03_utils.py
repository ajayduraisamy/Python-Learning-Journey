# 03_utils.py
# Small helpers for feature formatting and CSV save

import pandas as pd
import os

def sample_to_dataframe(sample_list, feature_names):
    """
    sample_list: iterable of numeric features (len == number of features)
    feature_names: list of names
    returns: pandas DataFrame with single row
    """
    df = pd.DataFrame([sample_list], columns=feature_names)
    return df

def save_metrics(path, metrics_text):
    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(metrics_text)
