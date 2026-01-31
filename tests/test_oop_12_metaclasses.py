import pytest
import sys
import os

# Add concepts to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_exercise_structure():
    # Test that the exercise module has the expected structure
    from concepts.oop_12.SUBoop_12 import exercises as ex
    
    # Check that basic functions exist
    assert callable(ex.basic_function)
    assert callable(ex.advanced_function)
