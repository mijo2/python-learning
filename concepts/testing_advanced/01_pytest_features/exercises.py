# Pytest Advanced Features Exercises

import pytest

# Exercise: Write parameterized test for multiplication

def multiply(a, b):
    return a * b

# TODO: Use @pytest.mark.parametrize for multiply tests
# e.g., (2, 3, 6), (0, 5, 0)

# Uncomment to test
# def test_multiply(a, b, expected):
#     assert multiply(a, b) == expected