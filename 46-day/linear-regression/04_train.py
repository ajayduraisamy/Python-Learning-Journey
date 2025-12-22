# 04_train.py
# Training script for Linear Regression project

from 01_dataset import get_train_test
from 02_model import train_model, evaluate_model, save_model
from 03_utils import save_metrics

def main():
    X_train, X_test, y_train, y_test = get_train_test()
    print("Training samples:", len(X_train))
    print("Testing samples:", len(X_test))

    model = train_model(X_train, y_train)
    mae, mse, r2 = evaluate_model(model, X_test, y_test)

    print("MAE:", mae)
    print("MSE:", mse)
    print("R²:", r2)

    save_model(model)
    save_metrics("models/metrics.txt", f"MAE: {mae}\nMSE: {mse}\nR2: {r2}")

if __name__ == "__main__":
    main()
