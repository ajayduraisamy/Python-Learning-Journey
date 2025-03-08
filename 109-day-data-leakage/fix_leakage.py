import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

df = pd.DataFrame({
    "age": [22, 25, 47, 52, 46, 56],
    "salary": [20000, 25000, 70000, 80000, 65000, 90000],
    "target": [0, 0, 1, 1, 1, 1]
})

X = df[["age", "salary"]]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

#  Correct: preprocessing inside pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

pipeline.fit(X_train, y_train)

print("Model trained without data leakage")
