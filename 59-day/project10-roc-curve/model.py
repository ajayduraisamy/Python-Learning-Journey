from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from dataset import load_data

df = load_data()
X = df.drop("label", axis=1)
y = df["label"]

model = LogisticRegression()
model.fit(X, y)

probs = model.predict_proba(X)[:,1]
print("ROC AUC:", roc_auc_score(y, probs))
