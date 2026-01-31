"""
IMPORT SYSTEM INTERNALS — SOLUTIONS
"""

# Exercise 1: Check sys.modules
import sys
print("Ex1: 'sys' in sys.modules =", 'sys' in sys.modules)  # True

# Exercise 2: Import path
print("Ex2: Current dir in sys.path =", '.' in sys.path)  # False, usually not

# Exercise 3: Dynamic import
import importlib
mod = importlib.import_module('collections')
print("Ex3: hasattr(collections, 'Counter') =", hasattr(mod, 'Counter'))  # True

# Exercise 4: From import
from datetime import datetime
print("Ex4: datetime.now() =", datetime.now())  # current time

# Exercise 5: Import as
import json as js
print("Ex5: js.loads =", js.loads)  # <function>