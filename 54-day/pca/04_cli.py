# 04_cli.py
# CLI for training + PCA transformation

import argparse
import pandas as pd
from 03_train import main as train_main
from 02_model import load_pca, transform_data

def cmd_train(args):
    train_main()

def cmd_transform(args):
    try:
        pca = load_pca()
    except:
        print("PCA model not found. Train first!")
        return

    df = pd.DataFrame([[args.f1, args.f2, args.f3]], 
                      columns=["feature1","feature2","feature3"])

    result = transform_data(pca, df)[0]
    print("Reduced Vector:", result)

def main():
    parser = argparse.ArgumentParser(description="PCA CLI")
    sub = parser.add_subparsers(dest="cmd")

    sub.add_parser("train", help="Train PCA model")

    t = sub.add_parser("transform", help="Transform 3D vector to PCA space")
    t.add_argument("--f1", type=float, required=True)
    t.add_argument("--f2", type=float, required=True)
    t.add_argument("--f3", type=float, required=True)

    args = parser.parse_args()

    if args.cmd == "train":
        cmd_train(args)
    elif args.cmd == "transform":
        cmd_transform(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
