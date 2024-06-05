import pandas as pd
from sklearn.datasets import make_classification

def load_data(n=400):
    X, y = make_classification(
        n_samples=n,
        n_features=6,
        n_informative=4,
        random_state=42
    )
    df = pd.DataFrame(X, columns=[f"f{i}" for i in range(1,7)])
    df["label"] = y
    return df
