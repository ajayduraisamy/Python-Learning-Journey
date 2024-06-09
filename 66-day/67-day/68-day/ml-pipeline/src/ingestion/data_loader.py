# data_loader.py
# Load and validate raw dataset

import pandas as pd
from ingestion.schema import COLUMNS
from config.settings import config
from utils.logger import log

def load_raw():
    log("Loading raw CSV: " + config.RAW_DATA_PATH)
    df = pd.read_csv(config.RAW_DATA_PATH)

    if list(df.columns) != COLUMNS:
        log("WARNING: Column mismatch with schema")

    log("Loaded dataset with shape: " + str(df.shape))
    return df

if __name__ == "__main__":
    df = load_raw()
    print(df.head())
