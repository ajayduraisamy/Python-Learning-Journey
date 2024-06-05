from sklearn.datasets import make_classification
import pandas as pd

def load_data():
    X, y = make_classification(n_samples=300, n_features=2, n_redundant=0, n_clusters_per_class=1)
    df = pd.DataFrame(X, columns=["f1","f2"])
    df["label"] = y
    return df
