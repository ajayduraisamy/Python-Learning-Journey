# model_saver.py
# Saves ML models

import joblib
from utils.logger import log

def save_model(model, path):
    joblib.dump(model, path)
    log(f"Saved model → {path}")
