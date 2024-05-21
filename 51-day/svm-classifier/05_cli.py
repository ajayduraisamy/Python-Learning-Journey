# 05_cli.py
# CLI for training and prediction using SVM

import argparse
import pandas as pd
from 04_train import main as train_main
from 02_model import load_model

def cmd_train(args):
    train_main()

def cmd_predict(args):
    try:
        model = load_model(args.model or "models/svm.joblib")
    except Exception as e:
        print("Failed to load model:", e)
        return

    df = pd.DataFrame([[args.workout, args.calories]],
                      columns=["workout", "calories"])

    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]

    print("Prediction:", "FIT" if pred == 1 else "UNFIT")
    print("Probability of being FIT:", prob)

def main():
    parser = argparse.ArgumentParser(description="SVM Classifier CLI")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("train", help="Train SVM model")

    p = sub.add_parser("predict", help="Predict fitness")
    p.add_argument("--workout", type=float, required=True)
    p.add_argument("--calories", type=float, required=True)
    p.add_argument("--model", help="Model file path")

    args = parser.parse_args()

    if args.cmd == "train":
        cmd_train(args)
    elif args.cmd == "predict":
        cmd_predict(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
