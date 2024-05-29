from dataset import load_data

df = load_data()

Q1 = df["x"].quantile(0.25)
Q3 = df["x"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR

outliers = df[(df["x"] < lower) | (df["x"] > upper)]

print("Outliers found:")
print(outliers)
