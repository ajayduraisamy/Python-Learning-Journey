from sklearn.datasets import make_classification
import pandas as pd

def load_data():
    X, y = make_classification(n_samples=300, n_features=3)
    df = pd.DataFrame(X, columns=["a","b","c"])
    df["label"] = y
    return df
