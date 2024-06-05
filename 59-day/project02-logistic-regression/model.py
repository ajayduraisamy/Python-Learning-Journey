from sklearn.linear_model import LogisticRegression
from dataset import load_data

df = load_data()
X = df[["hours"]]
y = df["passed"]

model = LogisticRegression()
model.fit(X, y)

print("Prob passing with 6 hours study:", model.predict_proba([[6]])[0][1])
