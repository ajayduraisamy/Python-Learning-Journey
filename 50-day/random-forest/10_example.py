# 10_example.py
# Example manual test

from 04_train import main as train_main
from 02_model import load_model
import pandas as pd

train_main()

model = load_model()
df = pd.DataFrame([[50, 250, 140]], columns=["age","cholesterol","blood_pressure"])
pred = model.predict(df)[0]
print("Example:", "HIGH RISK" if pred == 1 else "LOW RISK")
