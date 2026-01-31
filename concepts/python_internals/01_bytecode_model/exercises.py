# Bytecode Model Exercises

import dis

# Exercise 1: Disassemble a simple function
# Create a function that multiplies two numbers and prints its bytecode.

# TODO: Define a multiply function and disassemble it
def multiply(a, b):
    return a * b

# Uncomment to see bytecode
# dis.dis(multiply)

# Exercise 2: Analyze conditional bytecode
# Write an if-else statement and disassemble it.

# TODO: Define a function with if-else
def check_positive(n):
    if n > 0:
        return "Positive"
    else:
        return "Not positive"

# Uncomment to see bytecode
# dis.dis(check_positive)