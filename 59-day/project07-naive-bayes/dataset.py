import numpy as np
import pandas as pd

def load_data(n=300):
    np.random.seed(42)
    happy = np.random.randint(0, 10, n)
    sad = np.random.randint(0, 10, n)
    label = (happy > sad).astype(int)
    return pd.DataFrame({"happy": happy, "sad": sad, "label": label})
