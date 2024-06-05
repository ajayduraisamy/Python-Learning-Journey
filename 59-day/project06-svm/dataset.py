from sklearn.datasets import make_classification
import pandas as pd

def load_data():
    X, y = make_classification(300, 2)
    df = pd.DataFrame(X, columns=["x","y"])
    df["label"] = y
    return df
