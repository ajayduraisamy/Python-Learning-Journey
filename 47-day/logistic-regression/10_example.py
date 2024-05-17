# 10_example.py
# Example usage

from 04_train import main as train_main
from 02_model import load_model
import pandas as pd

train_main()

model = load_model()
df = pd.DataFrame([[6, 7, 80]], columns=["hours_study", "hours_sleep", "prev_score"])
pred = model.predict(df)[0]
print("Example prediction:", "PASS" if pred == 1 else "FAIL")
