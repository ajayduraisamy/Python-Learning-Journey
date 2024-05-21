# 04_train.py
# Train the SVM classifier

from 01_dataset import get_train_test
from 02_model import train_model, evaluate_model, save_model
from 03_utils import save_metrics

def main():
    X_train, X_test, y_train, y_test = get_train_test()

    print("Training samples:", len(X_train))
    print("Testing samples:", len(X_test))

    model = train_model(X_train, y_train)

    acc, report = evaluate_model(model, X_test, y_test)
    print("Accuracy:", acc)
    print(report)

    save_model(model)
    save_metrics("models/metrics.txt", f"Accuracy: {acc}\n\n{report}")

if __name__ == "__main__":
    main()
