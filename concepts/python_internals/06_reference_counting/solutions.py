# Reference Counting Exercises Solutions

import sys

lst = [1, 2]
print("Initial:", sys.getrefcount(lst) - 1)
alias = lst
print("After alias:", sys.getrefcount(lst) - 1)
del alias
print("After del:", sys.getrefcount(lst) - 1)