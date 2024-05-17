# 05_cli.py
# CLI for training and predicting pass/fail

import argparse
from 04_train import main as train_main
from 02_model import load_model
import pandas as pd

def cmd_train(args):
    train_main()

def cmd_predict(args):
    try:
        model = load_model(args.model or "models/log_reg.joblib")
    except Exception as e:
        print("Model load failed:", e)
        return

    df = pd.DataFrame([[
        args.hours_study,
        args.hours_sleep,
        args.prev_score
    ]], columns=["hours_study", "hours_sleep", "prev_score"])

    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]

    print("Predicted:", "PASS" if pred == 1 else "FAIL")
    print("Probability of passing:", prob)

def main():
    parser = argparse.ArgumentParser(description="Logistic Regression CLI")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("train", help="Train model")

    p = sub.add_parser("predict", help="Predict pass/fail")
    p.add_argument("--hours_study", type=float, required=True)
    p.add_argument("--hours_sleep", type=float, required=True)
    p.add_argument("--prev_score", type=float, required=True)
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
