import os
from 01_dataset import generate_cm_dataset
from 02_model import train_model, plot_confusion_matrix

def main():
    df = generate_cm_dataset()
    X = df[["f1","f2"]]
    y = df["label"]

    model = train_model(X, y)
    fig = plot_confusion_matrix(model, X, y)

    os.makedirs("outputs", exist_ok=True)
    fig.savefig("outputs/confusion_matrix.png")
    print("Saved: outputs/confusion_matrix.png")

if __name__ == "__main__":
    main()
