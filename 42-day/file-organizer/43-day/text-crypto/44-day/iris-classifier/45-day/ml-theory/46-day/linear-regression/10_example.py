# 10_example.py
# Example usage

from 04_train import main as train_main
from 02_model import load_model
import pandas as pd

train_main()

model = load_model()
df = pd.DataFrame([[1500, 3, 10]], columns=["sqft", "bedrooms", "age"])
pred = model.predict(df)[0]
print("Predicted example price:", pred)
