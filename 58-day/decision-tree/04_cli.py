# 04_cli.py
# CLI to run decision tree visualizer

import argparse
from 03_train import main as train_main

def main():
    parser = argparse.ArgumentParser(description="Decision Tree Visualizer CLI")
    parser.add_argument("cmd", choices=["train"])
    args = parser.parse_args()

    if args.cmd == "train":
        train_main()

if __name__ == "__main__":
    main()
