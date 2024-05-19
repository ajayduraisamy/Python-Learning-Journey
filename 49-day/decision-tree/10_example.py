# 10_example.py
# Example usage

from 04_train import main as train_main
from 02_model import load_model
import pandas as pd

train_main()

model = load_model()
df = pd.DataFrame([[25, 70000, 15]], columns=["age","income","browse_time"])
pred = model.predict(df)[0]
print("Example:", "BOUGHT" if pred == 1 else "NOT BOUGHT")
