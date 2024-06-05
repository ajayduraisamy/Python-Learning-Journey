from sklearn.tree import DecisionTreeClassifier
from dataset import load_data

df = load_data()
X = df[["a","b","c"]]
y = df["label"]

model = DecisionTreeClassifier()
model.fit(X, y)

print("Prediction:", model.predict([[0,1,2]])[0])
