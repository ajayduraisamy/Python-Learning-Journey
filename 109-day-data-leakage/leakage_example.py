import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Dummy dataset
df = pd.DataFrame({
    "age": [22, 25, 47, 52, 46, 56],
    "salary": [20000, 25000, 70000, 80000, 65000, 90000],
    "target": [0, 0, 1, 1, 1, 1]
})

X = df[["age", "salary"]]
y = df["target"]

#  WRONG: scaling before train-test split (leakage)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

print("Model trained with data leakage")
