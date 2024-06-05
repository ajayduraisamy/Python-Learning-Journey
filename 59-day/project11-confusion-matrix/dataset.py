from sklearn.datasets import make_classification
import pandas as pd

def load_data():
    X, y = make_classification(300, 3)
    df = pd.DataFrame(X, columns=["f1","f2","f3"])
    df["label"] = y
    return df
