"""
02 CUSTOM ITERATORS — SOLUTIONS
"""

# Exercise 1: Create a Range Iterator
class RangeIterator:
    """Custom iterator for range-like functionality"""
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

# Exercise 2: Create a Fibonacci Iterator
class FibonacciIterator:
    """Iterator that generates Fibonacci numbers"""
    def __init__(self, count):
        self.count = count
        self.a, self.b = 0, 1
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.count:
            raise StopIteration
        self.index += 1
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

# Exercise 3: Create a Lines Iterator (for file reading)
class LinesIterator:
    """Iterator that reads lines from a list (simulating file reading)"""
    def __init__(self, lines):
        self.lines = lines
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.lines):
            raise StopIteration
        line = self.lines[self.index]
        self.index += 1
        return line.strip()

if __name__ == "__main__":
    # Test Range Iterator
    print("Range Iterator (1-5):")
    for num in RangeIterator(1, 6):
        print(num, end=' ')
    print()

    # Test Fibonacci Iterator
    print("Fibonacci Iterator (first 8 numbers):")
    for num in FibonacciIterator(8):
        print(num, end=' ')
    print()

    # Test Lines Iterator
    print("Lines Iterator:")
    lines = ["  Line 1  ", "Line 2", "  Line 3  "]
    for line in LinesIterator(lines):
        print(f"'{line}'")
