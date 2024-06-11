# pipeline_saver.py
# Save preprocessing pipeline using joblib

import joblib
from utils.logger import log

def save_pipeline(pipeline, path="artifacts/preprocessing.pkl"):
    log("Saving preprocessing pipeline...")
    joblib.dump(pipeline, path)
    log(f"Saved → {path}")
