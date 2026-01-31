"""
MONKEY PATCHING RISKS — SOLUTIONS
"""

# Exercise 1: Patch a function
def func():
    return "original"

print("Ex1: Before patch:", func())
original = func
func = lambda: "patched"
print("Ex1: After patch:", func())
func = original
print("Ex1: Restored:", func())

# Exercise 2: Patch list.append (risky)
original_append = list.append
list.append = lambda self, x: None  # Breaks functionality
lst = [1, 2]
lst.append(3)
print("Ex2: lst after bad append:", lst)  # [1, 2] - broken!
list.append = original_append
lst.append(3)
print("Ex2: After restore:", lst)  # [1, 2, 3]

# Exercise 3: Add method
class Test:
    pass

t = Test()
Test.greet = lambda self: "Hello"
print("Ex3: t.greet():", t.greet())

# Exercise 4: Patching os.path.join (breaks other code)
import os
original_path = os.path.join
os.path.join = lambda *args: "patched"
print("Ex4: os.path.join('a', 'b'):", os.path.join('a', 'b'))  # broken
os.path.join = original_path
print("Ex4: Restored:", os.path.join('a', 'b'))  # a/b

# Exercise 5: Safer patching with context
from unittest.mock import patch

def risky_func():
    return "risky"

print("Ex5: Before:", risky_func())
with patch('__main__.risky_func', return_value="safe"):
    print("Ex5: Inside patch:", risky_func())
print("Ex5: After:", risky_func())  # Back to normal