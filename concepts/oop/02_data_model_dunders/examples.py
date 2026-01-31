# Data Model and Dunder Methods Examples

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"{self.name} ({self.breed})"

    def __repr__(self):
        return f"Dog(name='{self.name}', breed='{self.breed}')"

my_dog = Dog("Buddy", "Golden Retriever")
print(str(my_dog))   # Buddy (Golden Retriever)
print(repr(my_dog))  # Dog(name='Buddy', breed='Golden Retriever')

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __eq__(self, other):
        if not isinstance(other, Dog):
            return NotImplemented
        return self.name == other.name and self.breed == other.breed

    def __hash__(self):
        return hash((self.name, self.breed))

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Buddy", "Golden Retriever")
print(dog1 == dog2)  # True
print(hash(dog1) == hash(dog2))  # True