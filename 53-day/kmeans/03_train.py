# 03_train.py
# Train K-Means model

from 01_dataset_utils import get_data, save_metrics
from 02_model import train_model, evaluate_model, save_model

def main():
    X = get_data()
    print("Samples:", len(X))

    model = train_model(X)

    score = evaluate_model(model, X)
    print("Silhouette Score:", score)

    save_model(model)
    save_metrics("models/metrics.txt", f"Silhouette Score: {score}")

if __name__ == "__main__":
    main()
