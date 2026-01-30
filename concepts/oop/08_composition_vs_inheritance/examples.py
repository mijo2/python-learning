# Composition vs Inheritance Examples

# Inheritance
class Engine:
    def start(self):
        print("Engine started")

class Car(Engine):
    pass

car = Car()
car.start()

# Composition
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

car = Car()
car.start()