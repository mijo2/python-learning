# Class Decorators Examples

def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Config:
    def __init__(self, env):
        self.env = env

c1 = Config("dev")
c2 = Config("prod")
print(c1.env)  # dev
print(c2.env)  # dev (same instance)

# Adding methods
def add_repr(cls):
    cls.__repr__ = lambda self: f"{cls.__name__}({self.__dict__})"
    return cls

@add_repr
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
print(repr(p))  # Point({'x': 1, 'y': 2})