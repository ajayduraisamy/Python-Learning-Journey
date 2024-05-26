# 04_cli.py
# CLI to generate decision boundary image

import argparse
from 03_train import main as train_main

def main():
    parser = argparse.ArgumentParser(description="Decision Boundary CLI")
    parser.add_argument("cmd", choices=["train"], help="Run training & generate image")

    args = parser.parse_args()
    if args.cmd == "train":
        train_main()

if __name__ == "__main__":
    main()
