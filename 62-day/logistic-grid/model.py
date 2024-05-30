from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from dataset import load_data

df = load_data()
X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

params = {
    "C": [0.1, 1, 10],
    "solver": ["liblinear", "lbfgs"]
}

model = LogisticRegression(max_iter=500)
grid = GridSearchCV(model, params, cv=5)
grid.fit(X_train, y_train)

best = grid.best_estimator_
preds = best.predict(X_test)

print("Best Params:", grid.best_params_)
print("Logistic Regression Accuracy:", accuracy_score(y_test, preds))
