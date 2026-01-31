"""
MODULE CACHING — SOLUTIONS
"""

# Exercise 1: Cache size
import sys
print("Ex1: sys.modules size =", len(sys.modules))  # Varies

# Exercise 2: Import and check
import collections
print("Ex2: 'collections' in sys.modules =", 'collections' in sys.modules)  # True

# Exercise 3: Re-import
import collections  # again
print("Ex3: Re-imported, still cached")  # No change

# Exercise 4: Identity
import re
import re as r
print("Ex4: re is r =", re is r)  # True

# Exercise 5: Delete and re-import
print("Ex5: Before delete, 're' in sys.modules =", 're' in sys.modules)  # True
del sys.modules['re']
print("Ex5: After delete, 're' in sys.modules =", 're' in sys.modules)  # False
import re  # re-import
print("Ex5: After re-import, 're' in sys.modules =", 're' in sys.modules)  # True