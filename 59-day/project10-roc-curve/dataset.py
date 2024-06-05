from sklearn.datasets import make_classification
import pandas as pd

def load_data():
    X, y = make_classification(300, 4)
    df = pd.DataFrame(X, columns=["a","b","c","d"])
    df["label"] = y
    return df
