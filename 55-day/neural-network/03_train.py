# 03_train.py
# Train the neural network on XOR dataset

from 01_dataset_utils import get_train_test, save_output
from 02_model import train_model, evaluate_model, save_model

def main():
    X_train, X_test, y_train, y_test = get_train_test()

    print("Training samples:", len(X_train))
    print("Testing samples:", len(X_test))

    model = train_model(X_train, y_train)

    acc, rep = evaluate_model(model, X_test, y_test)
    print("Accuracy:", acc)
    print(rep)

    save_model(model)
    save_output("models/metrics.txt", f"Accuracy: {acc}\n\n{rep}")

if __name__ == "__main__":
    main()
