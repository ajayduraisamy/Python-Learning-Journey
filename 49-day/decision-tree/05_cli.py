# 05_cli.py
# CLI for training + prediction using decision tree

import argparse
import pandas as pd
from 04_train import main as train_main
from 02_model import load_model

def cmd_train(args):
    train_main()

def cmd_predict(args):
    try:
        model = load_model(args.model or "models/decision_tree.joblib")
    except Exception as e:
        print("Failed to load model:", e)
        return

    df = pd.DataFrame([[args.age, args.income, args.browse_time]],
                      columns=["age", "income", "browse_time"])

    pred = model.predict(df)[0]
    print("Prediction:", "BOUGHT" if pred == 1 else "NOT BOUGHT")

def main():
    parser = argparse.ArgumentParser(description="Decision Tree CLI")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("train", help="Train the model")

    p = sub.add_parser("predict", help="Predict customer purchase")
    p.add_argument("--age", type=int, required=True)
    p.add_argument("--income", type=float, required=True)
    p.add_argument("--browse_time", type=float, required=True)
    p.add_argument("--model", help="Model path")

    args = parser.parse_args()

    if args.cmd == "train":
        cmd_train(args)
    elif args.cmd == "predict":
        cmd_predict(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
