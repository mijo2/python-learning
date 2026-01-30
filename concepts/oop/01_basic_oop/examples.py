# Basic OOP Examples

class Dog:
    def __init__(self, name, breed):
        self.name = name  # instance attribute
        self.breed = breed

    def bark(self):  # instance method
        return f"{self.name} says woof!"

# Creating an instance
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.bark())  # Output: Buddy says woof!