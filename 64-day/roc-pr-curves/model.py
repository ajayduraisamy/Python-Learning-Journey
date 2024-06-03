from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc, precision_recall_curve
from sklearn.ensemble import RandomForestClassifier
from dataset import load_data
import matplotlib.pyplot as plt

df = load_data()
X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)

probs = model.predict_proba(X_test)[:,1]

# ROC
fpr, tpr, _ = roc_curve(y_test, probs)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr)
plt.title(f"ROC Curve (AUC={roc_auc:.2f})")
plt.xlabel("FPR")
plt.ylabel("TPR")
plt.savefig("roc_curve.png")

# PR Curve
precision, recall, _ = precision_recall_curve(y_test, probs)
plt.figure()
plt.plot(recall, precision)
plt.title("Precision-Recall Curve")
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.savefig("pr_curve.png")

print("ROC AUC:", roc_auc)
