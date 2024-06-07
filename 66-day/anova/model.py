from sklearn.feature_selection import f_classif
from dataset import load_data
import pandas as pd

df = load_data()
X = df.drop("label", axis=1)
y = df["label"]

F_vals, p_vals = f_classif(X, y)

print("ANOVA F-values:")
print(pd.Series(F_vals, index=X.columns))

print("\nP-values:")
print(pd.Series(p_vals, index=X.columns))
