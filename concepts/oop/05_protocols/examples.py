# Protocols Examples

from typing import Protocol

class Speakable(Protocol):
    def speak(self) -> str:
        ...

class Dog:
    def speak(self) -> str:
        return "Woof!"

class Car:
    def speak(self) -> str:
        return "Vroom!"

def make_sound(obj: Speakable) -> str:
    return obj.speak()

dog = Dog()
car = Car()
print(make_sound(dog))  # Woof!
print(make_sound(car))  # Vroom!