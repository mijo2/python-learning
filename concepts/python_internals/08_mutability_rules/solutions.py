"""
MUTABILITY RULES — SOLUTIONS
"""

# Exercise 1: Immutable strings
# Strings are immutable, so s + "3" creates a new string
s = "python"
t = s
s = s + "3"
print("Ex1:", s, t)  # python3 python

# Exercise 2: Mutable lists
# Lists are mutable, b and a refer to the same list
a = [1, 2, 3]
b = a
a[0] = 99
print("Ex2:", a, b)  # [99, 2, 3] [99, 2, 3]

# Exercise 3: Tuple with mutable elements
# Tuple itself is immutable, but its elements can be mutable
tup = (1, 2, [3, 4])
tup[2].append(5)
print("Ex3:", tup)  # (1, 2, [3, 4, 5])

# Exercise 4: Function with mutable default
# Use None as default and check inside
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print("Ex4:", add_item(1))  # [1]
print("Ex4:", add_item(2))  # [2]

# Exercise 5: Copying lists
# Use slice to create shallow copy
original = [1, 2, 3]
copy_list = original[:]
original.append(4)
print("Ex5:", original, copy_list)  # [1, 2, 3, 4] [1, 2, 3]

# Exercise 6: Nested mutability
# Shallow copy doesn't copy nested mutables
nested = [[1, 2], [3, 4]]
nested_copy = nested[:]
nested[0].append(99)
print("Ex6:", nested, nested_copy)  # [[1, 2, 99], [3, 4]] [[1, 2, 99], [3, 4]]

# To fix, use deep copy
import copy
nested_deep = [[1, 2], [3, 4]]
nested_deep_copy = copy.deepcopy(nested_deep)
nested_deep[0].append(100)
print("Deep copy:", nested_deep, nested_deep_copy)  # [[1, 2, 100], [3, 4]] [[1, 2], [3, 4]]