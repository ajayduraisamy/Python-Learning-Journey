# 05_cli.py
# CLI for training + predicting high-risk status

import argparse
import pandas as pd
from 04_train import main as train_main
from 02_model import load_model

def cmd_train(args):
    train_main()

def cmd_predict(args):
    try:
        model = load_model(args.model or "models/random_forest.joblib")
    except Exception as e:
        print("Model load failed:", e)
        return

    df = pd.DataFrame([[args.age, args.cholesterol, args.bp]],
                      columns=["age", "cholesterol", "blood_pressure"])

    pred = model.predict(df)[0]
    print("Prediction:", "HIGH RISK" if pred == 1 else "LOW RISK")

def main():
    parser = argparse.ArgumentParser(description="Random Forest CLI")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("train", help="Train model")

    p = sub.add_parser("predict", help="Predict risk")
    p.add_argument("--age", type=int, required=True)
    p.add_argument("--cholesterol", type=int, required=True)
    p.add_argument("--bp", type=int, required=True)
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
