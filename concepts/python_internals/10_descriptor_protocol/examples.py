def run():
    print("=== Descriptor Protocol Examples ===\n")

    # Example 1: Simple descriptor
    print("1. Simple descriptor:")
    class SimpleDescriptor:
        def __init__(self, value):
            self.value = value

        def __get__(self, instance, owner):
            if instance is None:
                return self
            return self.value

        def __set__(self, instance, value):
            self.value = value

    class MyClass:
        attr = SimpleDescriptor("default")

    obj = MyClass()
    print(f"obj.attr: {obj.attr}")
    obj.attr = "changed"
    print(f"obj.attr: {obj.attr}")

    # Example 2: Property descriptor
    print("\n2. Using property:")
    class Person:
        def __init__(self, name):
            self._name = name

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, value):
            if not isinstance(value, str):
                raise ValueError("Name must be string")
            self._name = value

    p = Person("Alice")
    print(f"p.name: {p.name}")
    p.name = "Bob"
    print(f"p.name: {p.name}")
    # p.name = 123  # ValueError

    # Example 3: Static method (non-data descriptor)
    print("\n3. Static method:")
    class Math:
        @staticmethod
        def add(x, y):
            return x + y

    print(f"Math.add(2, 3): {Math.add(2, 3)}")
    m = Math()
    print(f"m.add(4, 5): {m.add(4, 5)}")

    # Example 4: Class method
    print("\n4. Class method:")
    class Counter:
        count = 0

        @classmethod
        def increment(cls):
            cls.count += 1
            return cls.count

    print(f"Counter.increment(): {Counter.increment()}")
    print(f"Counter.increment(): {Counter.increment()}")

if __name__ == "__main__":
    run()