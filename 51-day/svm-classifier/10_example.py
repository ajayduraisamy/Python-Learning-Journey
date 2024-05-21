# 10_example.py
# Example usage for SVM

from 04_train import main as train_main
from 02_model import load_model
import pandas as pd

train_main()

model = load_model()
df = pd.DataFrame([[6, 2300]], columns=["workout", "calories"])
pred = model.predict(df)[0]
print("Example:", "FIT" if pred == 1 else "UNFIT")
