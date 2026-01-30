# Mixins Exercises Solutions

class Serializable:
    def save(self):
        print("Data saved")

class Loggable:
    def log(self, message):
        print(f"Logging: {message}")

    def save(self):
        self.log("Saving data")
        super().save()

    def load(self):
        self.log("Loading data")
        print("Data loaded")

class DataHandler(Serializable, Loggable):
    def __init__(self, data):
        self.data = data

# Test
handler = DataHandler([1,2,3])
handler.save()  # Logging: Saving data \n Data saved
handler.load()  # Logging: Loading data \n Data loaded