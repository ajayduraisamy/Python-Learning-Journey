# 02_model.py
# Decision Tree model: train, evaluate, save, load

import os
import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

def train_model(X_train, y_train):
    model = DecisionTreeClassifier(max_depth=5)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    report = classification_report(y_test, preds)
    return acc, report

def save_model(model, path="models/decision_tree.joblib"):
    folder = os.path.dirname(path)
    os.makedirs(folder, exist_ok=True)
    joblib.dump(model, path)
    return path

def load_model(path="models/decision_tree.joblib"):
    return joblib.load(path)
