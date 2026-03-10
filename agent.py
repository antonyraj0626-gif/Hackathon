import sys
import os
import subprocess

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from modes.quickfix import quickfix
from modes.deepfix import deepfix
from language_detector import detect_language


def run_agent(file, mode):
    language = detect_language(file)
    print("\n===== Cognifix Debug Agent =====")
    print("Detected language:", language)

    # Read code lines once
    with open(file, "r") as f:
        code_lines = f.readlines()

    # Pre-run QuickFix (optional)
    if mode == "quickfix":
        print("\nPre-run QuickFix check...")
        quickfix(file)
        with open(file, "r") as f:
            code_lines = f.readlines()

    attempts = 0
    while attempts < 5:
        if language != "python":
            print("Currently, only Python is supported for hackathon demo.")
            return

        # Run Python program
        result = subprocess.run(["python", file], capture_output=True, text=True)

        if result.returncode == 0:
            print("\nProgram executed successfully!\n")
            print(result.stdout)
            return

        error = result.stderr
        print("\nError detected:\n")
        print(error)

        if mode == "quickfix":
            confirm = input("\nApply QuickFix? (y/n): ").strip().lower()
            if confirm == "y":
                quickfix(file, error)
        elif mode == "deepfix":
            deepfix(file, error, code_lines)
            confirm = input("\nApply QuickFix for this error? (y/n): ").strip().lower()
            if confirm == "y":
                quickfix(file, error)

        # Re-read code lines after possible fixes
        with open(file, "r") as f:
            code_lines = f.readlines()

        attempts += 1

    print("\nUnable to fix after multiple attempts.")