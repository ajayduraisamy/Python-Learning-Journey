from sklearn.decomposition import PCA
from dataset import load_data

df = load_data()
X = df

pca = PCA(n_components=2)
X2 = pca.fit_transform(X)

print("Reduced shape:", X2.shape)
