import pandas as pd
from sklearn.datasets import make_classification

def load_data(n=400, random_state=42):
    X, y = make_classification(
        n_samples=n,
        n_features=5,
        n_informative=3,
        n_redundant=0,
        random_state=random_state
    )
    df = pd.DataFrame(X, columns=[f"f{i}" for i in range(1,6)])
    df["label"] = y
    return df
