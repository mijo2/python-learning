# Metaclasses Exercises Solutions

import time

class TimestampMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['created_at'] = time.time()
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=TimestampMeta):
    pass

# Test
print(MyClass.created_at)