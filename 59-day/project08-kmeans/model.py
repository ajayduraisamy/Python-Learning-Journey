from sklearn.cluster import KMeans
from dataset import load_data

df = load_data()
X = df[["x","y"]]

model = KMeans(n_clusters=3)
model.fit(X)

print("Cluster:", model.predict([[2,2]])[0])
