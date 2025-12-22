# 10_example.py
# Quick example: train and make a prediction programmatically

from 04_train import main as train_main
from 02_model import load_model
from 01_data import load_dataset
from 03_utils import sample_to_dataframe

# Train
train_main()

# Load and predict example
model = load_model()
X, _, feature_names, target_names = load_dataset()
sample = [5.1, 3.5, 1.4, 0.2]  # example for setosa
df = sample_to_dataframe(sample, feature_names)
pred = model.predict(df)
print("Predicted:", target_names[int(pred[0])])
