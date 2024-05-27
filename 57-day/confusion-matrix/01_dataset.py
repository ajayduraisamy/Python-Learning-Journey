from sklearn.datasets import make_classification
import pandas as pd

def generate_cm_dataset():
    X, y = make_classification(
        n_samples=400,
        n_features=2,
        n_redundant=0,
        n_clusters_per_class=1,
        random_state=42
    )
    df = pd.DataFrame(X, columns=["f1","f2"])
    df["label"] = y
    return df
