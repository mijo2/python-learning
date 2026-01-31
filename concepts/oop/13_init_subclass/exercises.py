# __init_subclass__ Exercises

# Exercise: __init_subclass__
# Use __init_subclass__ to register subclasses in a list.

# TODO: Implement base class with __init_subclass__
class Registry:
    subclasses = []

    def __init_subclass__(cls, **kwargs):
        pass

class SubClass1(Registry):
    pass

class SubClass2(Registry):
    pass

# Test
# print(Registry.subclasses)  # Should contain SubClass1 and SubClass2