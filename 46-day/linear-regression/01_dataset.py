# 01_dataset.py
# Generate synthetic dataset for house price prediction

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def generate_dataset(n=200, random_state=42):
    np.random.seed(random_state)
    sqft = np.random.randint(500, 3000, n)
    bedrooms = np.random.randint(1, 5, n)
    age = np.random.randint(1, 30, n)

    noise = np.random.normal(0, 15000, n)

    price = sqft * 120 + bedrooms * 20000 - age * 500 + noise
    
    df = pd.DataFrame({
        "sqft": sqft,
        "bedrooms": bedrooms,
        "age": age,
        "price": price
    })
    return df

def get_train_test(test_size=0.2):
    df = generate_dataset()
    X = df[["sqft", "bedrooms", "age"]]
    y = df["price"]
    return train_test_split(X, y, test_size=test_size, random_state=42)
