# Mixins Pattern Examples

class JSONMixin:
    def to_json(self):
        return f"{{'data': {self.data}}}"

class LoggerMixin:
    def log(self, message):
        print(f"Log: {message}")

class DataProcessor(JSONMixin, LoggerMixin):
    def __init__(self, data):
        self.data = data

    def process(self):
        self.log("Processing data")
        return self.to_json()

processor = DataProcessor([1, 2, 3])
print(processor.process())