# Slots Exercises

# Exercise: Slots
# Modify a class to use __slots__ for memory efficiency.

# TODO: Add __slots__ to a class
class OptimizedClass:
    __slots__ = ['a', 'b']
    def __init__(self, a, b):
        self.a = a
        self.b = b