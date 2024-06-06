from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from dataset import load_data
import pandas as pd

df = load_data()
X = df.drop("label", axis=1)
y = df["label"]

print("Before Undersampling:")
print(df["label"].value_counts())

rus = RandomUnderSampler()
X_res, y_res = rus.fit_resample(X, y)

print("\nAfter Undersampling:")
print(pd.Series(y_res).value_counts())

X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("\nClassification Report:")
print(classification_report(y_test, pred))
