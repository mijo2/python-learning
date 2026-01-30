# Protocols Exercises Solutions

from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None:
        ...

class Text:
    def __init__(self, content):
        self.content = content

    def draw(self):
        print(f"Drawing text: {self.content}")

class Image:
    def __init__(self, filename):
        self.filename = filename

    def draw(self):
        print(f"Drawing image: {self.filename}")

def render(obj: Drawable):
    obj.draw()

# Test
text = Text("Hello")
img = Image("pic.png")
render(text)  # Drawing text: Hello
render(img)   # Drawing image: pic.png