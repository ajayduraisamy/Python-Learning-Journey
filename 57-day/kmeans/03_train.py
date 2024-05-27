import os
from 01_dataset import generate_kmeans_dataset
from 02_model import train_kmeans, plot_clusters

def main():
    X = generate_kmeans_dataset()
    model = train_kmeans(X)
    fig = plot_clusters(model, X)

    os.makedirs("outputs", exist_ok=True)
    fig.savefig("outputs/kmeans_clusters.png")
    print("Saved: outputs/kmeans_clusters.png")

if __name__ == "__main__":
    main()
