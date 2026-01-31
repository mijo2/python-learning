# Multiple Inheritance and MRO Exercises

# Exercise: Multiple Inheritance and MRO
# Create classes A, B, C where C inherits from A and B.
# Each has a 'greet' method. Ensure MRO is followed.

# TODO: Implement classes
class A:
    pass

class B:
    pass

class C(A, B):
    pass

# Test
# c = C()
# c.greet()  # Should print based on MRO