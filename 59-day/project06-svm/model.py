from sklearn.svm import SVC
from dataset import load_data

df = load_data()
X = df[["x","y"]]
y = df["label"]

model = SVC(probability=True)
model.fit(X, y)

print("Prediction:", model.predict([[0.1, -0.2]])[0])
