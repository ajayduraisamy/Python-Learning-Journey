# 02_model.py
# Linear Regression model training, evaluation, save/load

import os
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    mse = mean_squared_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    return mae, mse, r2

def save_model(model, path="models/linear_reg.joblib"):
    folder = os.path.dirname(path)
    os.makedirs(folder, exist_ok=True)
    joblib.dump(model, path)
    return path

def load_model(path="models/linear_reg.joblib"):
    return joblib.load(path)
