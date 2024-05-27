import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

def train_kmeans(X, k=3):
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(X)
    return model

def plot_clusters(model, X):
    labels = model.labels_
    fig, ax = plt.subplots()
    sns.scatterplot(x=X["x"], y=X["y"], hue=labels, palette="tab10", ax=ax)
    centers = model.cluster_centers_
    ax.scatter(centers[:,0], centers[:,1], s=200, c="black", marker="X")
    ax.set_title("KMeans Clusters")
    return fig
