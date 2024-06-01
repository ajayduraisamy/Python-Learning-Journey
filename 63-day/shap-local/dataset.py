from sklearn.datasets import make_classification
import pandas as pd

def load_data():
    X, y = make_classification(
        n_samples=400,
        n_features=5,
        n_informative=3,
        random_state=42
    )
    df = pd.DataFrame(X, columns=["f1","f2","f3","f4","f5"])
    df["label"] = y
    return df
