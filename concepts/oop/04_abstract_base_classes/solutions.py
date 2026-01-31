# Abstract Base Classes Exercises Solutions

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Test
circle = Circle(5)
rect = Rectangle(4, 6)
print(circle.area())  # ~78.53981633974483
print(rect.area())    # 24