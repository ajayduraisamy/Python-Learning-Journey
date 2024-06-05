from catboost import CatBoostClassifier
from dataset import load_data
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = load_data()
X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = CatBoostClassifier(
    iterations=200,
    depth=4,
    learning_rate=0.1,
    verbose=False
)

model.fit(X_train, y_train)
preds = model.predict(X_test)

print("CatBoost Accuracy:", accuracy_score(y_test, preds))
