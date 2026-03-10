def deepfix(file, error, code_lines):
    """
    DeepFix:
    1. Explain the error clearly
    2. Show a suggested fix
    3. Ask user whether to apply the fix
    4. If yes -> apply fix, run code, show output
    5. If no -> stop terminal
    """
    import subprocess

    print("\n===== DeepFix Analysis =====\n")
    fixed_line = None
    line_no = None

    try:
        if "SyntaxError: expected ':'" in error:
            print("Explanation: Python expected a ':' at the end of a statement (for, if, while, def).")
            line_no = int(error.split("line")[1].split()[0]) - 1
            faulty_line = code_lines[line_no].rstrip()
            fixed_line = faulty_line + ":"

        elif "IndentationError" in error:
            print("Explanation: Python relies on indentation (spaces/tabs) to define blocks.")
            line_no = int(error.split("line")[1].split()[0]) - 1
            faulty_line = code_lines[line_no].rstrip()
            # Suggest proper indentation (4 spaces)
            fixed_line = "    " + faulty_line

        elif "ModuleNotFoundError" in error:
            module_name = error.split("'")[1]
            print(f"Explanation: The module '{module_name}' is missing.")
            print(f"Suggested fix: Install it using 'pip install {module_name}'")
            return  # Cannot auto-fix missing module offline

        else:
            print("Explanation: General runtime error. Inspect your code carefully.")
            return

        # Show faulty vs suggested fix
        print(f"\nFaulty line : {code_lines[line_no].rstrip()}")
        print(f"Suggested fix: {fixed_line}")

        # Ask user to apply fix
        confirm = input("\nApply this fix? (y/n): ").strip().lower()
        if confirm == "y":
            code_lines[line_no] = fixed_line + "\n"
            with open(file, "w") as f:
                f.writelines(code_lines)
            print("\nFix applied! Executing program...\n")
            # Run program after applying fix
            result = subprocess.run(
                ["python", file], capture_output=True, text=True
            )
            if result.returncode == 0:
                print("Program executed successfully!\n")
                print(result.stdout)
            else:
                print("Error after applying fix:\n")
                print(result.stderr)
        else:
            print("\nFix not applied. Exiting terminal.\n")
            exit()

    except Exception as e:
        print(f"Could not parse error or apply fix.\nOriginal error:\n{error}")
        print(f"Exception: {e}")