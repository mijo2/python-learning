# Memory Layout Examples

import sys

class Regular:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Slotted:
    __slots__ = ['a', 'b']
    def __init__(self, a, b):
        self.a = a
        self.b = b

reg = Regular(1, 2)
slo = Slotted(1, 2)

print("Regular size:", sys.getsizeof(reg))
print("Slotted size:", sys.getsizeof(slo))
print("List size:", sys.getsizeof([1, 2, 3]))
print("Dict size:", sys.getsizeof({'a': 1, 'b': 2}))