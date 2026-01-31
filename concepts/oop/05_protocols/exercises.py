# Protocols Exercises

# Exercise: Protocols
# Define a Protocol 'Drawable' with method 'draw'.
# Create classes 'Text' and 'Image' that implement Drawable.
# Write a function that takes a Drawable and calls draw.

# TODO: Implement Protocol and classes
from typing import Protocol

class Drawable(Protocol):
    pass

class Text:
    pass

class Image:
    pass

def render(obj):
    pass

# Test
# text = Text("Hello")
# img = Image("pic.png")
# render(text)  # Should print "Drawing text: Hello"
# render(img)   # Should print "Drawing image: pic.png"