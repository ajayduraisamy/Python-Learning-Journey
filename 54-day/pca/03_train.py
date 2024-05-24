# 03_train.py
# Train PCA model and save variance info

from 01_dataset_utils import get_data, save_output
from 02_model import train_pca, save_pca

def main():
    X = get_data()
    print("Samples:", len(X))

    pca = train_pca(X)

    save_pca(pca)

    variance = pca.explained_variance_ratio_
    print("Explained Variance:", variance)

    save_output("models/variance.txt", f"Explained Variance: {variance}")

if __name__ == "__main__":
    main()
