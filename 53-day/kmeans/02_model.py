# 02_model.py
# K-Means: train, save, load

import os
import joblib
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def train_model(X, k=3):
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(X)
    return model

def evaluate_model(model, X):
    labels = model.labels_
    score = silhouette_score(X, labels)
    return score

def save_model(model, path="models/kmeans.joblib"):
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, path)

def load_model(path="models/kmeans.joblib"):
    return joblib.load(path)
