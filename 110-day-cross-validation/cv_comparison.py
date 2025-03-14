from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.linear_model import LogisticRegression

X, y = load_iris(return_X_y=True)
model = LogisticRegression(max_iter=200)

# Holdout
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
model.fit(X_train, y_train)
holdout_score = model.score(X_test, y_test)

# K-Fold
kf = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(model, X, y, cv=kf)

print("Holdout accuracy:", holdout_score)
print("K-Fold mean accuracy:", cv_scores.mean())
