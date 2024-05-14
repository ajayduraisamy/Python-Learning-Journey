# 04_train.py
# Script to train the Iris classifier end-to-end

from 01_data import get_train_test, load_dataset
from 02_model import train_model, evaluate_model, save_model
from 03_utils import save_metrics

def main():
    X_train, X_test, y_train, y_test = get_train_test()
    print("Training on", len(X_train), "samples, testing on", len(X_test))
    model = train_model(X_train, y_train)
    acc, report = evaluate_model(model, X_test, y_test)
    print("Accuracy:", acc)
    print(report)
    save_path = save_model(model)
    print("Model saved to", save_path)
    save_metrics("models/metrics.txt", f"Accuracy: {acc}\n\n{report}")

if __name__ == "__main__":
    main()
