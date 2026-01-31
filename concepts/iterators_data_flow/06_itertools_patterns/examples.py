
def run():
    print("=== 06 ITERTOOLS PATTERNS Examples ===
")

    # Example 1: Basic iterator
    print("1. Basic Iterator:")
    print("   class MyIterator:")
    print("       def __iter__(self):")
    print("           return self")
    print("       def __next__(self):")
    print("           # return next item or raise StopIteration")

    print()

    # Example 2: Generator function
    print("2. Generator Function:")
    print("   def fibonacci(n):")
    print("       a, b = 0, 1")
    print("       for _ in range(n):")
    print("           yield a")
    print("           a, b = b, a + b")

    print()

    # Example 3: Iterator tools
    print("3. Iterator Tools:")
    print("   from itertools import count, cycle, chain")
    print("   counter = count(start=10)")
    print("   colors = cycle(['red', 'green', 'blue'])")
    print("   combined = chain([1, 2], [3, 4])")

if __name__ == "__main__":
    run()
