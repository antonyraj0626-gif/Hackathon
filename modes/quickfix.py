def quickfix(file, error=""):
    """
    QuickFix for Python:
    - Adds missing colons for def/if/for/while
    - Fixes indentation for blocks after def/if/for/while
    - Corrects simple typos like 'sqr(' -> 'square('
    """
    print("\nScanning for QuickFixable issues...\n")

    with open(file, "r") as f:
        lines = f.readlines()

    fixed = []
    skip_next = False
    for i, line in enumerate(lines):
        s = line.rstrip()

        # Fix missing colon
        if s.startswith(("def ", "if ", "for ", "while ")) and not s.endswith(":"):
            line = line.rstrip() + ":\n"

        # Ensure next line is indented if previous line is a block starter
        if i > 0:
            prev_line = lines[i-1].rstrip()
            if prev_line.endswith(":") and not s.startswith("    ") and s != "":
                line = "    " + line.lstrip()

        # Fix known typos
        line = line.replace("sqr(", "square(")
        line = line.replace("numppy", "numpy")
        line = line.replace("panadas", "pandas")

        fixed.append(line)

    with open(file, "w") as f:
        f.writelines(fixed)

    print("QuickFix applied!\n")