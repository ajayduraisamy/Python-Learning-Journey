# 02_model.py
# SVM model: train, evaluate, save, load

import os
import joblib
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

def train_model(X_train, y_train, kernel="rbf"):
    model = SVC(kernel=kernel, probability=True, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    report = classification_report(y_test, preds)
    return acc, report

def save_model(model, path="models/svm.joblib"):
    folder = os.path.dirname(path)
    os.makedirs(folder, exist_ok=True)
    joblib.dump(model, path)
    return path

def load_model(path="models/svm.joblib"):
    return joblib.load(path)
