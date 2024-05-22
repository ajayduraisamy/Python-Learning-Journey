# 02_model.py
# Naive Bayes model: train, evaluate, save/load

import joblib
import os
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

def train_model(X_train, y_train):
    model = GaussianNB()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    rep = classification_report(y_test, preds)
    return acc, rep

def save_model(model, path="models/nb.joblib"):
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, path)

def load_model(path="models/nb.joblib"):
    return joblib.load(path)
