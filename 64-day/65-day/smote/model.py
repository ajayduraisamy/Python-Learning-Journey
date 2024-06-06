from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
from dataset import load_data

df = load_data()
X = df.drop("label", axis=1)
y = df["label"]

print("Before SMOTE:")
print(df["label"].value_counts())

sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X, y)

print("\nAfter SMOTE:")
print(pd.Series(y_res).value_counts())

X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("\nClassification Report:")
print(classification_report(y_test, pred))
