# 05_cli.py
# CLI to train and predict pass/fail using KNN

import argparse
import pandas as pd
from 04_train import main as train_main
from 02_model import load_model

def cmd_train(args):
    train_main()

def cmd_predict(args):
    try:
        model = load_model(args.model or "models/knn.joblib")
    except Exception as e:
        print("Error loading model:", e)
        return

    df = pd.DataFrame([[args.hours_study, args.anxiety]],
                      columns=["hours_study", "anxiety"])

    pred = model.predict(df)[0]
    print("Prediction:", "PASS" if pred == 1 else "FAIL")

def main():
    parser = argparse.ArgumentParser(description="KNN Classifier CLI")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("train", help="Train the model")

    p = sub.add_parser("predict", help="Predict pass/fail")
    p.add_argument("--hours_study", type=float, required=True)
    p.add_argument("--anxiety", type=float, required=True)
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
