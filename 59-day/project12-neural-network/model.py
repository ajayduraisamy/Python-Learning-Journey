from sklearn.neural_network import MLPClassifier
from dataset import load_data

df = load_data()
X = df[["x1","x2"]]
y = df["label"]

model = MLPClassifier(hidden_layer_sizes=(4,2), max_iter=1000)
model.fit(X, y)

print("XOR prediction:", model.predict([[1,0]])[0])
