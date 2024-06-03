from sklearn.datasets import make_regression
import pandas as pd

def load_data():
    X, y = make_regression(
        n_samples=400,
        n_features=4,
        noise=20,
        random_state=42
    )
    df = pd.DataFrame(X, columns=["f1","f2","f3","f4"])
    df["target"] = y
    return df
