# Class Decorators Exercises Solutions

def add_version(cls):
    cls.version = "1.0"
    return cls

@add_version
class MyClass:
    pass

print(MyClass.version)  # 1.0