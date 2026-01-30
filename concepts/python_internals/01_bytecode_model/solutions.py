# Bytecode Model Exercises Solutions

import dis

# Exercise 1: Disassemble a simple function
def multiply(a, b):
    return a * b

print("Bytecode for multiply:")
dis.dis(multiply)

# Exercise 2: Analyze conditional bytecode
def check_positive(n):
    if n > 0:
        return "Positive"
    else:
        return "Not positive"

print("\nBytecode for check_positive:")
dis.dis(check_positive)