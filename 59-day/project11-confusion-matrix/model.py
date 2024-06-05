from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from dataset import load_data

df = load_data()
X = df[["f1","f2","f3"]]
y = df["label"]

model = LogisticRegression(max_iter=500)
model.fit(X, y)

preds = model.predict(X)
print(confusion_matrix(y, preds))
