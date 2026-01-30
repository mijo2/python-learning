# Class Decorators Exercises

# Exercise: Create a class decorator that adds a class attribute

def add_version(cls):
    cls.version = "1.0"
    return cls

# TODO: Apply @add_version to a class and print the version
# Uncomment
# @add_version
# class MyClass:
#     pass

# print(MyClass.version)