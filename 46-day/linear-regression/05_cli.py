# 05_cli.py
# CLI for training and predicting house prices

import argparse
from 04_train import main as train_main
from 02_model import load_model
import pandas as pd

def cmd_train(args):
    train_main()

def cmd_predict(args):
    try:
        model = load_model(args.model or "models/linear_reg.joblib")
    except Exception as e:
        print("Error loading model:", e)
        return

    values = [args.sqft, args.bedrooms, args.age]
    df = pd.DataFrame([values], columns=["sqft", "bedrooms", "age"])
    pred = model.predict(df)[0]
    print("Predicted Price:", pred)

def main():
    parser = argparse.ArgumentParser(description="Linear Regression CLI")
    sub = parser.add_subparsers(dest="cmd")

    t = sub.add_parser("train", help="Train the model")

    p = sub.add_parser("predict", help="Predict house price")
    p.add_argument("--sqft", type=float, required=True)
    p.add_argument("--bedrooms", type=int, required=True)
    p.add_argument("--age", type=int, required=True)
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
