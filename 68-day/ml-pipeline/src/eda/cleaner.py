# cleaner.py
# Data cleaning operations

import pandas as pd
from utils.logger import log
from config.settings import config

def clean(df):
    log("Cleaning dataset...")

    # 1. Remove duplicates
    before = len(df)
    df = df.drop_duplicates()
    log(f"Removed duplicates: {before - len(df)}")

    # 2. Check missing values
    missing = df.isnull().sum()
    log("Missing values per column:")
    log(str(missing))

    # No missing values expected in this dataset,
    # but we include logic for safety.
    df = df.fillna(0)

    # Save clean dataset
    df.to_csv(config.CLEAN_DATA_PATH, index=False)
    log("Saved cleaned dataset → " + config.CLEAN_DATA_PATH)

    return df
