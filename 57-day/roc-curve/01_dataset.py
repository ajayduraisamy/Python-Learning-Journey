from sklearn.datasets import make_classification
import pandas as pd

def generate_roc_dataset():
    X, y = make_classification(
        n_samples=400,
        n_features=4,
        n_redundant=0,
        random_state=42
    )
    df = pd.DataFrame(X, columns=["f1","f2","f3","f4"])
    df["label"] = y
    return df
