# 03_train.py
# Train model + export decision boundary image

from 01_dataset_utils import get_train_test, save_image
from 02_model import train_model, plot_decision_boundary

def main():
    X_train, X_test, y_train, y_test = get_train_test()

    print("Training model...")
    model = train_model(X_train, y_train)

    print("Generating decision boundary...")
    fig = plot_decision_boundary(model, X_train, y_train)

    save_image("outputs/decision_boundary.png", fig)
    print("Saved: outputs/decision_boundary.png")

if __name__ == "__main__":
    main()
