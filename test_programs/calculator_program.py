# calculator_program.py - intentionally broken
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(add(5, 3))
print(subtract(10, 4))
print(multiply(3, 7))
print(divide(10, 0))
