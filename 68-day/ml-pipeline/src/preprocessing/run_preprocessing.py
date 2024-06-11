# run_preprocessing.py
# Complete preprocessing step:
# load clean → split → FP → SMOTE → save pipeline

from eda.cleaner import clean
from ingestion.data_loader import load_raw
from preprocessing.splitter import split_dataset
from preprocessing.preprocess import build_preprocessing_pipeline
from preprocessing.pipeline_saver import save_pipeline
from utils.logger import log
from config.settings import config
from imblearn.over_sampling import SMOTE

def run():
    log("=== Running Preprocessing Stage ===")

    df = load_raw()
    df = clean(df)

    X_train, X_val, X_test, y_train, y_val, y_test = split_dataset(df)

    pipe, X_train_fe = build_preprocessing_pipeline(X_train)

    X_train_transformed = pipe.fit_transform(X_train_fe)

    log("Applying SMOTE...")
    sm = SMOTE(random_state=42)
    X_train_resampled, y_train_resampled = sm.fit_resample(X_train_transformed, y_train)

    log(f"Train before SMOTE: {len(y_train)}, after: {len(y_train_resampled)}")

    save_pipeline(pipe)

    log("=== Preprocessing Completed ===")

    return X_train_resampled, y_train_resampled

if __name__ == "__main__":
    run()
