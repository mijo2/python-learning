"""
03 PARAMETERIZED TESTS — SOLUTIONS
"""

import pytest

# Exercise 1: Simple parameterized test
@pytest.mark.parametrize("input_val,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
])
def test_double(input_val, expected):
    """Test doubling function with parameters"""
    assert input_val * 2 == expected

# Exercise 2: String operations
@pytest.mark.parametrize("input_str,expected", [
    ("hello", "HELLO"),
    ("WORLD", "WORLD"),
    ("Python", "PYTHON"),
    ("", ""),
])
def test_uppercase(input_str, expected):
    """Test uppercase conversion"""
    assert input_str.upper() == expected

# Exercise 3: Multiple parameters
@pytest.mark.parametrize("a,b,operation,expected", [
    (1, 2, "add", 3),
    (5, 3, "subtract", 2),
    (4, 5, "multiply", 20),
    (10, 2, "divide", 5),
])
def test_calculator(a, b, operation, expected):
    """Test calculator with multiple parameters"""
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        result = a // b
    assert result == expected

# Exercise 4: Implement the test functions (without pytest decorators)
def double(n):
    return n * 2

def uppercase(s):
    return s.upper()

def calculator(a, b, operation):
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x // y,
    }
    return operations[operation](a, b)

if __name__ == "__main__":
    # Run the parameterized tests manually
    print("Running parameterized tests manually:")

    # Test double
    for input_val, expected in [(1, 2), (2, 4), (3, 6)]:
        result = double(input_val)
        print(f"double({input_val}) = {result}, expected {expected}: {'PASS' if result == expected else 'FAIL'}")

    # Test uppercase
    for input_str, expected in [("hello", "HELLO"), ("WORLD", "WORLD"), ("Python", "PYTHON"), ("", "")]:
        result = uppercase(input_str)
        print(f"uppercase('{input_str}') = '{result}', expected '{expected}': {'PASS' if result == expected else 'FAIL'}")

    # Test calculator
    for a, b, operation, expected in [(1, 2, "add", 3), (5, 3, "subtract", 2), (4, 5, "multiply", 20), (10, 2, "divide", 5)]:
        result = calculator(a, b, operation)
        print(f"calculator({a}, {b}, '{operation}') = {result}, expected {expected}: {'PASS' if result == expected else 'FAIL'}")
