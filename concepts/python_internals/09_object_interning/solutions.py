"""
OBJECT INTERNING — SOLUTIONS
"""

# Exercise 1: Integers
# Small integers are interned
a = 42
b = 42
print("Ex1: a is b =", a is b)  # True

# Large integers are not
c = 1000
d = 1000
print("Ex1: c is d =", c is d)  # False

# Exercise 2: Strings
# Short strings are interned
s1 = "test"
s2 = "test"
print("Ex2: s1 is s2 =", s1 is s2)  # True

# Strings with spaces may not be
s3 = "test case"
s4 = "test case"
print("Ex2: s3 is s4 =", s3 is s4)  # False

# Exercise 3: Using intern
# sys.intern forces interning
import sys
key1 = sys.intern("unique_key")
key2 = sys.intern("unique_key")
print("Ex3: key1 is key2 =", key1 is key2)  # True

# Exercise 4: Lists
# Lists are mutable, not interned
lst1 = [1, 2]
lst2 = [1, 2]
print("Ex4: lst1 is lst2 =", lst1 is lst2)  # False
print("Ex4: lst1 == lst2 =", lst1 == lst2)  # True

# Exercise 5: Float
# Small floats may be interned in some implementations
f1 = 1.0
f2 = 1.0
print("Ex5: f1 is f2 =", f1 is f2)  # True in CPython

# Exercise 6: Tuple
# Small tuples are interned
t1 = (1, 2)
t2 = (1, 2)
print("Ex6: t1 is t2 =", t1 is t2)  # True