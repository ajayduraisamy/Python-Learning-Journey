from 03_train import main as train_main
from 02_model import load_model
import pandas as pd

train_main()
model = load_model()
df = pd.DataFrame([[1, 0]], columns=["x1","x2"])
print("Example:", model.predict(df)[0])
