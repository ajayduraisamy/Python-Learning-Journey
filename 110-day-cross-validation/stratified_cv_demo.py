from sklearn.datasets import make_classification
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
import numpy as np

X, y = make_classification(
    n_samples=1000,
    n_features=10,
    weights=[0.9, 0.1],  # imbalanced
    random_state=42
)

model = LogisticRegression(max_iter=300)

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=skf)

print("Class distribution:", np.bincount(y))
print("Stratified K-Fold accuracy:", scores.mean())
