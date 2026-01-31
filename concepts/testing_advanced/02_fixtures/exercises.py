"""
02 FIXTURES — EXERCISES

Instructions:
- Implement the following exercises with TODO guidance
- Each exercise shows what needs to be implemented
- Test your implementations after completion
"""


# Exercise 1: Basic fixture creation
# TODO: Create pytest fixtures for test data
import pytest

@pytest.fixture
def sample_data():
    """Provide sample test data"""
    # TODO: Return test data dictionary
    pass

def test_with_fixture(sample_data):
    """Test using fixture data"""
    # TODO: Use fixture data in assertions
    pass

# Exercise 2: Mocking demonstration
# TODO: Use unittest.mock to replace dependencies
from unittest.mock import Mock

def mocking_demo():
    """Demonstrate mocking"""
    # TODO: Create mock object
    # TODO: Configure mock behavior
    # TODO: Use mock in place of real object
    pass

# Exercise 3: Property-based testing basics
# TODO: Create simple property-based tests
def property_test_demo():
    """Basic property testing"""
    # TODO: Create function to test
    # TODO: Write property-based test cases
    pass
