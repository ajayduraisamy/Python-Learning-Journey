from sklearn.datasets import make_classification
import pandas as pd

def load_data():
    X, y = make_classification(400, 5, n_redundant=0)
    df = pd.DataFrame(X, columns=["f1","f2","f3","f4","f5"])
    df["label"] = y
    return df
