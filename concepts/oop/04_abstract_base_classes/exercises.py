# Abstract Base Classes Exercises

# Exercise: Abstract Base Classes
# Create an ABC 'Shape' with abstract method 'area'.
# Implement concrete classes 'Circle' and 'Rectangle' that inherit from Shape.

# TODO: Implement Shape ABC and subclasses
from abc import ABC, abstractmethod

class Shape(ABC):
    pass

class Circle(Shape):
    pass

class Rectangle(Shape):
    pass

# Test
# circle = Circle(5)
# rect = Rectangle(4, 6)
# print(circle.area())  # ~78.54
# print(rect.area())    # 24