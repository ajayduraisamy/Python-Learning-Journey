from sklearn.ensemble import RandomForestClassifier
from dataset import load_data
import pandas as pd

df = load_data()
X = df.drop("label", axis=1)
y = df["label"]

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X, y)

importance = model.feature_importances_

print("Feature Importances:")
print(pd.Series(importance, index=X.columns))
