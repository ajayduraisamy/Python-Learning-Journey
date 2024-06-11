# preprocess.py
# Scaling + feature engineering + SMOTE

import pandas as pd
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from utils.logger import log

def build_preprocessing_pipeline(X_train):
    log("Building preprocessing pipeline...")

    # === Feature Engineering ===
    X_train = X_train.copy()
    X_train["Hour"] = (X_train["Time"] / 3600).astype(int)

    numeric_features = [c for c in X_train.columns if c != "Hour"]

    transformers = [
        ("scale_pca", StandardScaler(), [c for c in numeric_features if c.startswith("V")]),
        ("scale_amount", RobustScaler(), ["Amount"]),
        ("scale_time", MinMaxScaler(), ["Time"]),
        ("pass_hour", "passthrough", ["Hour"])
    ]

    preprocessor = ColumnTransformer(transformers)

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
    ])

    return pipeline, X_train
