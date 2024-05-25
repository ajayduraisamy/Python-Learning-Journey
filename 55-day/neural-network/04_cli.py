# 04_cli.py
# CLI for NN train + predict

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
        print("Model not found. Please train first!")
        return

    df = pd.DataFrame([[args.x1, args.x2]], columns=["x1","x2"])
    pred = model.predict(df)[0]
    print("Prediction (XOR output):", pred)

def main():
    parser = argparse.ArgumentParser(description="Neural Network CLI")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("train", help="Train the neural network")

    p = sub.add_parser("predict", help="Predict XOR output")
    p.add_argument("--x1", type=int, required=True)
    p.add_argument("--x2", type=int, required=True)

    args = parser.parse_args()

    if args.cmd == "train":
        cmd_train(args)
    elif args.cmd == "predict":
        cmd_predict(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
