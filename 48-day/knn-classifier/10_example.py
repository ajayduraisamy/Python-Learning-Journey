# 10_example.py
# Example manual usage of KNN model

from 04_train import main as train_main
from 02_model import load_model
import pandas as pd

train_main()

model = load_model()
df = pd.DataFrame([[7, 3]], columns=["hours_study", "anxiety"])
pred = model.predict(df)[0]
print("Example:", "PASS" if pred == 1 else "FAIL")
