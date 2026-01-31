"""
Tests for list_comprehensions exercises.
"""

import pytest
import sys
import os

# Add concepts to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_exercise_1():
    import concepts.list_comprehensions.exercises as ex
    expected = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert ex.result1 == expected

def test_exercise_2():
    import concepts.list_comprehensions.exercises as ex
    expected = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    assert ex.result2 == expected

def test_exercise_3():
    import concepts.list_comprehensions.exercises as ex
    expected = ["python", "is", "fun"]
    assert ex.result3 == expected

def test_exercise_4():
    import concepts.list_comprehensions.exercises as ex
    expected = [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64)]
    assert ex.result4 == expected

def test_exercise_5():
    import concepts.list_comprehensions.exercises as ex
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    assert ex.result5 == expected

def test_exercise_6():
    import concepts.list_comprehensions.exercises as ex
    expected = [3, 0, 5, 0, 2]
    assert ex.result6 == expected

def test_exercise_7():
    import concepts.list_comprehensions.exercises as ex
    expected = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    assert ex.result7 == expected

def test_exercise_8():
    import concepts.list_comprehensions.exercises as ex
    expected = [4, 2, 4]
    assert ex.result8 == expected