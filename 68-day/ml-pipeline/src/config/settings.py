# settings.py
# Global configuration for ML pipeline

import os

class Config:
    PROJECT_NAME = "Credit Card Fraud Detection Pipeline"
    RAW_DATA_PATH = "data/raw/creditcard.csv"
    CLEAN_DATA_PATH = "data/clean/cleaned.csv"
    LOG_PATH = "logs/pipeline.log"

config = Config()
