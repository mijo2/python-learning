"""
04 CLASS DECORATORS — EXERCISES

Instructions:
- Learn about class decorators and their applications
- Create decorators that modify class behavior
- Understand when to use class vs function decorators
"""

# Exercise 1: Simple class decorator
# TODO: Create a decorator that adds a class attribute
def add_version(cls):
    """Decorator that adds version attribute to class"""
    # TODO: Add version attribute to class
    # TODO: Return the modified class
    pass

@add_version
class MyClass:
    """A simple class to be decorated"""
    def __init__(self, value):
        self.value = value

# Exercise 2: Class decorator with parameters
# TODO: Create a decorator that accepts parameters
def add_metadata(**kwargs):
    """Parameterized decorator that adds metadata to class"""
    def decorator(cls):
        # TODO: Add kwargs as attributes to class
        # TODO: Return modified class
        pass
    return decorator

@add_metadata(version="1.0", author="Student")
class DocumentedClass:
    """Class with metadata"""
    pass

# Exercise 3: Class decorator for method enhancement
# TODO: Create decorator that modifies class methods
def add_method_logging(cls):
    """Decorator that adds logging to all methods"""
    # TODO: Iterate through class attributes
    # TODO: Wrap methods with logging
    # TODO: Preserve method metadata
    # TODO: Return modified class
    pass

@add_method_logging
class LoggedClass:
    """Class with logged methods"""
    def method1(self):
        return "method1 result"

    def method2(self, param):
        return f"method2 result: {param}"

# Exercise 4: Singleton class decorator
# TODO: Create decorator that enforces singleton pattern
def singleton(cls):
    """Decorator that makes class a singleton"""
    instances = {}

    def get_instance(*args, **kwargs):
        # TODO: Check if instance exists
        # TODO: Create instance if needed
        # TODO: Return existing instance
        pass

    return get_instance

@singleton
class DatabaseConnection:
    """Singleton database connection"""
    def __init__(self, host="localhost"):
        self.host = host
        self.connected = True

# Test code (uncomment after implementation)
# if __name__ == "__main__":
#     print("=== Class Decorators Demo ===\n")
#
#     # Test version decorator
#     print("1. Version Decorator:")
#     obj = MyClass(42)
#     print(f"MyClass version: {getattr(MyClass, 'version', 'Not set')}")
#
#     # Test metadata decorator
#     print("\n2. Metadata Decorator:")
#     print(f"DocumentedClass version: {getattr(DocumentedClass, 'version', 'Not set')}")
#     print(f"DocumentedClass author: {getattr(DocumentedClass, 'author', 'Not set')}")
#
#     # Test method logging decorator
#     print("\n3. Method Logging Decorator:")
#     logged_obj = LoggedClass()
#     print("Calling method1:")
#     result1 = logged_obj.method1()
#     print("Calling method2:")
#     result2 = logged_obj.method2("test")
#
#     # Test singleton decorator
#     print("\n4. Singleton Decorator:")
#     conn1 = DatabaseConnection("server1")
#     conn2 = DatabaseConnection("server2")
#     print(f"Same instance: {conn1 is conn2}")  # Should be True
#     print(f"Host: {conn1.host}")  # Should be "server1" (first call)
