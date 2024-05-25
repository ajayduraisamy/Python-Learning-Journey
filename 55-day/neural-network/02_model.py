# 02_model.py
# Neural Network (MLPClassifier) - train, evaluate, save/load

import joblib
import os
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report

def train_model(X_train, y_train):
    model = MLPClassifier(
        hidden_layer_sizes=(8, 4),
        activation="relu",
        max_iter=1000,
        random_state=42
    )
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    rep = classification_report(y_test, preds)
    return acc, rep

def save_model(model, path="models/nn.joblib"):
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, path)

def load_model(path="models/nn.joblib"):
    return joblib.load(path)
