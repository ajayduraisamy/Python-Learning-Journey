from sklearn.neighbors import KNeighborsClassifier
from dataset import load_data

df = load_data()
X = df[["f1","f2"]]
y = df["label"]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

print("Prediction:", model.predict([[0.5, -1]])[0])
