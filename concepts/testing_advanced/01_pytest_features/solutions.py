# Pytest Advanced Features Exercises Solutions

import pytest

def multiply(a, b):
    return a * b

@pytest.mark.parametrize("a,b,expected", [(2, 3, 6), (0, 5, 0), (-1, 4, -4)])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected