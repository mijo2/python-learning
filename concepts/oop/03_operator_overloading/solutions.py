# Operator Overloading Exercises Solutions

import math

class Fraction:
    def __init__(self, num, den):
        gcd = math.gcd(num, den)
        self.num = num // gcd
        self.den = den // gcd

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, scalar):
        if not isinstance(scalar, int):
            return NotImplemented
        return Fraction(self.num * scalar, self.den)

# Test
f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
print(f1 + f2)  # 5/6
print(f1 * 3)   # 3/2