"""
03 PROTOCOLS — EXERCISES

Instructions:
- Implement the following exercises with TODO guidance
- Each exercise shows what needs to be implemented
- Test your implementations after completion
"""


# Exercise 1: Define a simple protocol
# TODO: Create protocol for objects that can be drawn
from typing import Protocol

class Drawable(Protocol):
    # TODO: Define draw method signature
    pass

# Exercise 2: Implement protocol
# TODO: Create classes that implement the protocol
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    # TODO: Implement draw method
    pass

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    # TODO: Implement draw method
    pass

# Exercise 3: Use protocol in function
# TODO: Write function that accepts Drawable objects
def render_shapes(shapes):
    """Render all drawable shapes"""
    # TODO: Iterate through shapes
    # TODO: Call draw method on each
    pass

# Exercise 4: Runtime protocol checking
# TODO: Use isinstance with protocols
def is_drawable(obj):
    """Check if object implements Drawable protocol"""
    # TODO: Use isinstance with protocol
    pass
