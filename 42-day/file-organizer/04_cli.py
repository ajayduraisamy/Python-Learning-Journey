# 04_cli.py
# CLI interface for file organizer

import argparse
from .01_core import organize_files
from .03_scan import scan_files

def main():
    parser = argparse.ArgumentParser(description="File Organizer CLI")
    parser.add_argument("path", help="Base folder to organize")
    parser.add_argument("--preview", action="store_true", help="Preview files before organizing")
    args = parser.parse_args()

    if args.preview:
        print("Files in directory:")
        for f in scan_files(args.path):
            print(" -", f)
        return

    organize_files(args.path)
    print("Organization completed.")

if __name__ == "__main__":
    main()
