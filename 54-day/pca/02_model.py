# 02_model.py
# PCA: fit, transform, save, load

import joblib
import os
from sklearn.decomposition import PCA

def train_pca(X, components=2):
    pca = PCA(n_components=components)
    pca.fit(X)
    return pca

def transform_data(pca, X):
    return pca.transform(X)

def save_pca(pca, path="models/pca.joblib"):
    os.makedirs("models", exist_ok=True)
    joblib.dump(pca, path)

def load_pca(path="models/pca.joblib"):
    return joblib.load(path)
