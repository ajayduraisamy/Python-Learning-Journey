import pandas as pd

def load_data():
    return pd.DataFrame({
        "color": ["red", "blue", "green", "blue", "red"],
        "size": ["S", "M", "L", "M", "S"]
    })
