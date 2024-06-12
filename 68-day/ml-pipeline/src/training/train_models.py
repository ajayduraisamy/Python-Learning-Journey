# train_models.py
# Train Logistic Regression, RandomForest, GradientBoosting

import joblib
from preprocessing.run_preprocessing import run
from training.evaluate import evaluate_model
from training.model_saver import save_model
from training.model_selector import choose_best_model
from utils.logger import log
from config.settings import config

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

def train():
    log("=== Training Models ===")

    X_train, y_train = run()  # Preprocessed + SMOTE

    # Validation data not transformed yet → load raw & clean again
    from ingestion.data_loader import load_raw
    from eda.cleaner import clean
    from preprocessing.splitter import split_dataset
    from preprocessing.preprocess import build_preprocessing_pipeline

    df = clean(load_raw())
    X_train_raw, X_val_raw, X_test_raw, y_train_raw, y_val, y_test = split_dataset(df)
    pipe, X_train_fe = build_preprocessing_pipeline(X_train_raw)
    X_val_transformed = pipe.transform(X_val_raw.assign(Hour=(X_val_raw["Time"]/3600).astype(int)))

    models = {
        "logistic": LogisticRegression(max_iter=2000),
        "rf": RandomForestClassifier(n_estimators=200, random_state=42),
        "gb": GradientBoostingClassifier()
    }

    results = {}

    for name, model in models.items():
        log(f"Training model: {name}")
        model.fit(X_train, y_train)

        metrics = evaluate_model(model, X_val_transformed, y_val)

        save_model(model, f"artifacts/{name}.pkl")

        results[name] = {"model": model, "metrics": metrics}

    best = choose_best_model(results)
    save_model(results[best]["model"], "artifacts/best_model.pkl")

    log("=== Training Complete ===")

if __name__ == "__main__":
    train()
