# Metaclasses Exercises

# Exercise: Metaclasses
# Create a metaclass that adds a class attribute 'created_at' with timestamp.

# TODO: Implement metaclass
import time

class TimestampMeta(type):
    pass

class MyClass(metaclass=TimestampMeta):
    pass

# Test
# print(MyClass.created_at)