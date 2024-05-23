# 04_cli.py
# CLI for K-Means clustering predictions

import argparse
import pandas as pd
from 03_train import main as train_main
from 02_model import load_model

def cmd_train(args):
    train_main()

def cmd_predict(args):
    try:
        model = load_model()
    except:
        print("Model not found. Train first.")
        return

    df = pd.DataFrame([[args.x, args.y]], columns=["x", "y"])
    pred = model.predict(df)[0]
    print("Predicted Cluster:", pred)

def main():
    parser = argparse.ArgumentParser(description="KMeans CLI")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("train", help="Train model")

    p = sub.add_parser("predict", help="Predict cluster")
    p.add_argument("--x", type=float, required=True)
    p.add_argument("--y", type=float, required=True)

    args = parser.parse_args()

    if args.cmd == "train":
        cmd_train(args)
    elif args.cmd == "predict":
        cmd_predict(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
