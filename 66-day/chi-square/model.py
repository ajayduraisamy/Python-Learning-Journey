from sklearn.feature_selection import chi2
from dataset import load_data
import pandas as pd

df = load_data()
X = df.drop("label", axis=1)
y = df["label"]

chi_vals, p_vals = chi2(X, y)

print("Chi² Scores:")
print(pd.Series(chi_vals, index=X.columns))

print("\nP-values:")
print(pd.Series(p_vals, index=X.columns))
