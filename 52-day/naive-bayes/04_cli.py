# 04_cli.py
# CLI to train + predict sentiment (positive/negative)

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

    df = pd.DataFrame([[args.happy, args.sad]], columns=["happy", "sad"])
    pred = model.predict(df)[0]
    print("Sentiment:", "POSITIVE" if pred == 1 else "NEGATIVE")

def main():
    parser = argparse.ArgumentParser(description="Naive Bayes Classifier CLI")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("train", help="Train model")

    p = sub.add_parser("predict", help="Predict sentiment")
    p.add_argument("--happy", type=int, required=True)
    p.add_argument("--sad", type=int, required=True)

    args = parser.parse_args()

    if args.cmd == "train":
        cmd_train(args)
    elif args.cmd == "predict":
        cmd_predict(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
