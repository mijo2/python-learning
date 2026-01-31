# Composition vs Inheritance Exercises Solutions

# Assuming we have Engine and Car from earlier
# Instead of class Car(Engine), use composition

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