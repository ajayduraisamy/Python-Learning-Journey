from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.metrics import accuracy_score
from scipy.stats import randint
from dataset import load_data

df = load_data()
X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

params = {
    "n_estimators": randint(50, 300),
    "max_depth": randint(2, 20),
    "min_samples_split": randint(2, 10)
}

model = RandomForestClassifier()
rand = RandomizedSearchCV(model, params, n_iter=10, cv=5, random_state=42)
rand.fit(X_train, y_train)

best = rand.best_estimator_
preds = best.predict(X_test)

print("Best Params:", rand.best_params_)
print("Random Forest Accuracy:", accuracy_score(y_test, preds))
