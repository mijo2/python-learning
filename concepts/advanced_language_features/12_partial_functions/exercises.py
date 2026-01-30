# Partial Functions Exercises

from functools import partial

# Exercise: Use partial to create math operations

def operate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b

# TODO: Create add and subtract functions
# Uncomment
# add = partial(operate, op='+')
# subtract = partial(operate, op='-')
# print(add(5, 3))     # 8
# print(subtract(5, 3)) # 2