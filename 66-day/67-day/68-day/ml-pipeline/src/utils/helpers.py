# helpers.py
# Small utility functions shared across pipeline

import pandas as pd

def info(df, name="Dataset"):
    print(f"=== {name} Info ===")
    print(df.head())
    print(df.describe())
    print(df.isnull().sum())
