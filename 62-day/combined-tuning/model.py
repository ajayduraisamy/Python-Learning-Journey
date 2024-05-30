from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from dataset import load_data

df = load_data()
X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "logistic": (LogisticRegression(max_iter=500), {"C":[0.1,1,10]}),
    "svc": (SVC(probability=True), {"C":[0.1,1,10], "kernel":["rbf","linear"]})
}

for name, (model, params) in models.items():
    grid = GridSearchCV(model, params, cv=3)
    grid.fit(X_train, y_train)
    best = grid.best_estimator_
    preds = best.predict(X_test)
    print(f"{name} Best Params:", grid.best_params_)
    print(f"{name} Accuracy:", accuracy_score(y_test, preds))
    print("-----")
