"""
04 TYPEDDICT — EXERCISES

Instructions:
- Implement the following exercises with TODO guidance
- Each exercise shows what needs to be implemented
- Test your implementations after completion
"""


# Exercise 1: Define TypedDict
# TODO: Create TypedDict for person data
from typing import TypedDict

class Person(TypedDict):
    # TODO: Define required fields
    pass

# Exercise 2: Use TypedDict in functions
# TODO: Write functions that use TypedDict
def create_person(name, age, email):
    """Create person dictionary with type safety"""
    # TODO: Return properly typed dict
    pass

def display_person(person):
    """Display person information"""
    # TODO: Access typed fields safely
    pass

# Exercise 3: Optional fields
# TODO: Use NotRequired for optional fields
from typing import NotRequired

class ExtendedPerson(TypedDict, total=False):
    # TODO: Add required fields
    # TODO: Add optional fields with NotRequired
    pass
