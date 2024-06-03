from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from dataset import load_data

df = load_data()
X = df.drop("label", axis=1)
y = df["label"]

# Underfitting example (small model)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
small_model = RandomForestClassifier(n_estimators=5, max_depth=2)
small_model.fit(X_train, y_train)
small_preds = small_model.predict(X_test)

# Overfitting example (very deep model)
big_model = RandomForestClassifier(n_estimators=500, max_depth=None)
big_model.fit(X_train, y_train)
big_preds = big_model.predict(X_test)

print("Underfitting Accuracy:", accuracy_score(y_test, small_preds))
print("Overfitting Accuracy:", accuracy_score(y_test, big_preds))
