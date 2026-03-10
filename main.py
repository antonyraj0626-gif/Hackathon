import argparse
import os
from agent import run_agent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--mode", choices=["quickfix","deepfix"], default="quickfix")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        args.file = os.path.join("test_programs", args.file)

    print("\nStarting Cognifix...\n")
    run_agent(args.file, args.mode)

if __name__ == "__main__":
    main()