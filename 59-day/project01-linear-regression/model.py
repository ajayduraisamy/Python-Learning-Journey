from sklearn.linear_model import LinearRegression
from dataset import load_data

df = load_data()
X = df[["x"]]
y = df["y"]

model = LinearRegression()
model.fit(X, y)

print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Prediction for x=5:", model.predict([[5]])[0])
