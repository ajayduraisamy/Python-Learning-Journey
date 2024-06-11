# ML Pipeline — Credit Card Fraud Detection

## Run EDA:
python src/eda/eda_runner.py

## Run Preprocessing:
python src/preprocessing/run_preprocessing.py

This stage performs:
- Train/Val/Test split
- Scaling (Standard, Robust, MinMax)
- Feature engineering (Hour)
- SMOTE oversampling
- Pipeline saving to artifacts/preprocessing.pkl
