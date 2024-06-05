from sklearn.naive_bayes import GaussianNB
from dataset import load_data

df = load_data()
X = df[["happy","sad"]]
y = df["label"]

model = GaussianNB()
model.fit(X, y)

print("Prediction:", model.predict([[3,1]])[0])
