from sklearn.ensemble import RandomForestClassifier
from dataset import load_data

df = load_data()
X = df.drop("label", axis=1)
y = df["label"]

model = RandomForestClassifier()
model.fit(X, y)

print("Feature importance:", model.feature_importances_)
