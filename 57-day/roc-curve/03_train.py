import os
from 01_dataset import generate_roc_dataset
from 02_model import train_model, plot_roc

def main():
    df = generate_roc_dataset()
    X = df[["f1","f2","f3","f4"]]
    y = df["label"]

    model = train_model(X, y)
    fig = plot_roc(model, X, y)

    os.makedirs("outputs", exist_ok=True)
    fig.savefig("outputs/roc_curve.png")
    print("Saved: outputs/roc_curve.png")

if __name__ == "__main__":
    main()
