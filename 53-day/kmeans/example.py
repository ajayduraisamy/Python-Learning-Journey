from 03_train import main as train_main
from 02_model import load_model
import pandas as pd

train_main()
model = load_model()
df = pd.DataFrame([[8,2]], columns=["x","y"])
print("Example cluster:", model.predict(df)[0])
