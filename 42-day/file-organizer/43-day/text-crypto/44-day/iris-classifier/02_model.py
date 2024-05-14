# 02_model.py
# Train a simple classifier and evaluate

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

def train_model(X_train, y_train, n_estimators=100, random_state=42):
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    report = classification_report(y_test, preds)
    return acc, report

def save_model(model, path="models/iris_rf.joblib"):
    folder = path.rsplit("/", 1)[0]
    if folder and not folder == "":
        import os
        os.makedirs(folder, exist_ok=True)
    joblib.dump(model, path)
    return path

def load_model(path="models/iris_rf.joblib"):
    return joblib.load(path)
