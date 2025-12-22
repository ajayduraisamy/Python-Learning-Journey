# Iris Classifier (Day 44)

Beginner ML project — train a RandomForest on the Iris dataset.

## Setup
Create venv and install:
pip install -r requirements.txt

## Train
python -m 04_train

This trains the model, saves it to models/iris_rf.joblib and writes metrics to models/metrics.txt

## Predict
Provide a comma-separated sample of 4 features in the order:
sepal length (cm), sepal width (cm), petal length (cm), petal width (cm)

Example:
python -m 05_cli predict --sample "5.1,3.5,1.4,0.2"

## Files
- 01_data.py   : load dataset & splits
- 02_model.py  : training, evaluation, save/load
- 04_train.py  : training script
- 05_cli.py    : CLI for train/predict
