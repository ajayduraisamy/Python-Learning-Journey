from sklearn.datasets import make_classification
import pandas as pd

def load_data():
    X, y = make_classification(
        n_samples=700,
        n_features=5,
        n_informative=2,
        weights=[0.92, 0.08],
        random_state=42
    )
    df = pd.DataFrame(X, columns=[f"f{i}" for i in range(1,6)])
    df["label"] = y
    return df
