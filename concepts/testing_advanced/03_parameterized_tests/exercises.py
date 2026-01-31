"""
03 PARAMETERIZED TESTS — EXERCISES

Instructions:
- Learn about parameterized testing to avoid code duplication
- Implement test functions that work with multiple input combinations
"""

# Exercise 1: Create test data for parameterized tests
# TODO: Create a function that returns test data for multiple scenarios
def get_math_test_data():
    """
    Return test data for mathematical operations.
    Each tuple contains: (operation_name, a, b, expected_result)
    """
    # TODO: Return a list of tuples with test cases for:
    # - Addition: (2, 3, 5), (10, -5, 5), (0, 0, 0)
    # - Subtraction: (10, 3, 7), (5, 10, -5)
    # - Multiplication: (4, 5, 20), (7, 0, 0), (-3, -2, 6)
    # - Division: (10, 2, 5), (15, 3, 5)
    pass

# Exercise 2: Implement a calculator function
# TODO: Create a calculator that can handle different operations
def calculator(a, b, operation):
    """
    Perform a mathematical operation on two numbers.

    Args:
        a: First number
        b: Second number
        operation: String indicating operation ('add', 'subtract', 'multiply', 'divide')

    Returns:
        Result of the operation

    Raises:
        ValueError: For invalid operations or division by zero
    """
    # TODO: Implement addition
    # TODO: Implement subtraction
    # TODO: Implement multiplication
    # TODO: Implement division (handle division by zero)
    # TODO: Handle invalid operations
    pass

# Exercise 3: Create string processing functions
# TODO: Implement functions that process strings in different ways
def string_length_processor(text):
    """
    Process text and return its length.
    Handle edge cases like empty strings and None.
    """
    # TODO: Handle None input (return 0)
    # TODO: Handle empty string (return 0)
    # TODO: Return length of text
    pass

def string_case_processor(text, case_type):
    """
    Process text and change its case.

    Args:
        text: Input string
        case_type: 'upper', 'lower', or 'title'

    Returns:
        Processed string
    """
    # TODO: Handle None input (return empty string)
    # TODO: Implement 'upper' case conversion
    # TODO: Implement 'lower' case conversion
    # TODO: Implement 'title' case conversion
    # TODO: Handle invalid case_type
    pass

# Exercise 4: Create test data generators
# TODO: Create functions that generate test data for different scenarios
def generate_number_sequences():
    """
    Generate different sequences of numbers for testing.

    Returns:
        List of tuples: (description, sequence)
    """
    # TODO: Return test data for:
    # - Empty list: ([], "empty")
    # - Single element: ([42], "single")
    # - Positive numbers: ([1, 2, 3, 4, 5], "positive")
    # - Negative numbers: ([-1, -2, -3], "negative")
    # - Mixed numbers: ([-2, 0, 3, 7], "mixed")
    pass

def generate_string_samples():
    """
    Generate different string samples for testing.

    Returns:
        List of tuples: (description, string)
    """
    # TODO: Return test data for:
    # - Empty string: ("", "empty")
    # - Simple string: ("hello", "simple")
    # - String with spaces: ("hello world", "spaces")
    # - String with special chars: ("hello@world!", "special")
    # - Unicode string: ("héllo wörld", "unicode")
    pass

# Test code (uncomment after implementation)
# if __name__ == "__main__":
#     # Test calculator
#     test_data = get_math_test_data()
#     print("Calculator tests:")
#     for op, a, b, expected in test_data[:3]:  # Test first 3
#         result = calculator(a, b, op)
#         status = "PASS" if result == expected else "FAIL"
#         print(f"  {a} {op} {b} = {result} (expected {expected}) [{status}]")
#
#     # Test string processors
#     print("\nString processor tests:")
#     print(f"  Length of 'hello': {string_length_processor('hello')}")
#     print(f"  'hello' uppercased: {string_case_processor('hello', 'upper')}")
#     print(f"  'HELLO' lowercased: {string_case_processor('HELLO', 'lower')}")
#
#     # Test data generators
#     print("\nGenerated test data:")
#     print("Number sequences:")
#     for desc, seq in generate_number_sequences():
#         print(f"  {desc}: {seq}")
#
#     print("String samples:")
#     for desc, string in generate_string_samples():
#         print(f"  {desc}: '{string}'")
