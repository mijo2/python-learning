"""
02 LATE BINDING BEHAVIOR — EXERCISES

Instructions:
- Understand late binding behavior in closures and list comprehensions
- Learn how variable lookup works in nested scopes
- Implement solutions to common late binding problems
"""

# Exercise 1: Demonstrate late binding problem in list comprehension
# TODO: Create a list of functions that should return different values but don't
def create_functions_problem():
    """
    Create a list of functions using a loop.
    This demonstrates the late binding problem where all functions
    return the same value (the last value of the loop variable).
    """
    # TODO: Create an empty list for functions
    # TODO: Loop from 0 to 2
    # TODO: Create a lambda function that captures the loop variable
    # TODO: Append the lambda to the functions list
    # TODO: Return the list of functions
    pass

# Exercise 2: Fix late binding with default parameter
# TODO: Fix the late binding problem using default parameters
def create_functions_fixed_default():
    """
    Fix the late binding problem by using default parameters
    in lambda functions to capture the current value of the loop variable.
    """
    # TODO: Create empty list for functions
    # TODO: Loop from 0 to 2
    # TODO: Create lambda with default parameter capturing current i value
    # TODO: Append lambda to functions list
    # TODO: Return the list of functions
    pass

# Exercise 3: Fix late binding with closure
# TODO: Fix the late binding problem using a proper closure
def create_functions_fixed_closure():
    """
    Fix the late binding problem by creating a proper closure
    that captures the loop variable correctly.
    """
    # TODO: Create empty list for functions
    # TODO: Loop from 0 to 2
    # TODO: Define inner function that captures i
    # TODO: Append inner function to list
    # TODO: Return the list of functions
    pass

# Exercise 4: Late binding in class methods
# TODO: Demonstrate late binding in class method definitions
class CallbackManager:
    """
    A class that demonstrates late binding issues in method definitions.
    """

    def __init__(self):
        self.callbacks = []

    def add_callback(self, value):
        """
        Add a callback that should print the given value.
        Demonstrates late binding problem when using lambda in loop.
        """
        # TODO: Append lambda that captures value parameter
        # This will demonstrate the late binding problem
        pass

    def run_callbacks(self):
        """
        Execute all callbacks.
        """
        # TODO: Call each callback in self.callbacks
        pass

# Exercise 5: Fix late binding in class methods
# TODO: Fix the late binding problem in the CallbackManager class
class FixedCallbackManager:
    """
    A class that fixes the late binding problem in callback creation.
    """

    def __init__(self):
        self.callbacks = []

    def add_callback(self, value):
        """
        Add a callback that correctly captures the value parameter.
        """
        # TODO: Use proper closure or default parameter to fix late binding
        # TODO: Append the correctly capturing function
        pass

    def run_callbacks(self):
        """
        Execute all callbacks.
        """
        # TODO: Call each callback in self.callbacks
        pass

# Test code (uncomment after implementation)
# if __name__ == "__main__":
#     print("=== Late Binding Problem Demonstration ===")
#
#     # Test the problem
#     print("Problematic functions:")
#     functions = create_functions_problem()
#     for i, func in enumerate(functions):
#         print(f"  functions[{i}]() = {func()}")  # All return 2!
#
#     # Test the fixes
#     print("\nFixed with default parameter:")
#     functions_default = create_functions_fixed_default()
#     for i, func in enumerate(functions_default):
#         print(f"  functions[{i}]() = {func()}")  # Should return 0, 1, 2
#
#     print("\nFixed with closure:")
#     functions_closure = create_functions_fixed_closure()
#     for i, func in enumerate(functions_closure):
#         print(f"  functions[{i}]() = {func()}")  # Should return 0, 1, 2
#
#     # Test class methods
#     print("\n=== Class Method Late Binding ===")
#
#     print("Problematic callback manager:")
#     manager = CallbackManager()
#     for i in range(3):
#         manager.add_callback(i)
#     manager.run_callbacks()  # All print 2!
#
#     print("\nFixed callback manager:")
#     fixed_manager = FixedCallbackManager()
#     for i in range(3):
#         fixed_manager.add_callback(i)
#     fixed_manager.run_callbacks()  # Should print 0, 1, 2
