from sklearn.datasets import make_classification
import pandas as pd

def load_data():
    X, y = make_classification(
        n_samples=500,
        n_features=6,
        n_informative=3,
        random_state=42
    )
    df = pd.DataFrame(X, columns=[f"f{i}" for i in range(1,7)])
    df["label"] = y
    return df
