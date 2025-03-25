import pandas as pd
from sklearn.datasets import make_classification

# Create synthetic dataset
X, y = make_classification(
    n_samples=500,
    n_features=5,
    weights=[0.85, 0.15],
    random_state=42
)

df = pd.DataFrame(X, columns=[f"feature_{i}" for i in range(5)])
df["target"] = y

print(df.head())
print("Class distribution:")
print(df["target"].value_counts())
