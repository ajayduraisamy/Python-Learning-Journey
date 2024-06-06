from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE, RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from dataset import load_data

df = load_data()
X = df.drop("label", axis=1)
y = df["label"]

methods = {
    "SMOTE": SMOTE(),
    "Oversampling": RandomOverSampler(),
    "Undersampling": RandomUnderSampler()
}

for name, method in methods.items():
    X_res, y_res = method.fit_resample(X, y)
    X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    print(f"\n{name} F1 Score:", f1_score(y_test, preds))
