# 05_cli.py
# CLI to train and run predictions using the trained model

import argparse
from 01_data import load_dataset
from 02_model import load_model, train_model, save_model
from 03_utils import sample_to_dataframe
import sys

def cmd_train(args):
    import 04_train as trainer
    trainer.main()

def cmd_predict(args):
    try:
        model = load_model(args.model or "models/iris_rf.joblib")
    except Exception as e:
        print("Failed to load model:", e)
        sys.exit(1)
    X, _, feature_names, target_names = load_dataset()
    if args.sample:
        # expecting comma-separated values
        parts = [float(p.strip()) for p in args.sample.split(",")]
        if len(parts) != X.shape[1]:
            print(f"Expected {X.shape[1]} features, got {len(parts)}")
            sys.exit(1)
        df = sample_to_dataframe(parts, feature_names)
        pred = model.predict(df)
        print("Predicted label index:", int(pred[0]))
        print("Predicted label name:", target_names[int(pred[0])])
    else:
        print("Provide --sample with comma-separated feature values.")

def main():
    parser = argparse.ArgumentParser(description="Iris classifier CLI")
    sub = parser.add_subparsers(dest="cmd")

    t = sub.add_parser("train", help="Train the model")
    p = sub.add_parser("predict", help="Predict from sample")
    p.add_argument("--sample", "-s", help="Comma-separated feature values (4 values)")
    p.add_argument("--model", "-m", help="Path to trained model")

    args = parser.parse_args()

    if args.cmd == "train":
        cmd_train(args)
    elif args.cmd == "predict":
        cmd_predict(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
