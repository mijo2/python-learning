def run():
    print("=== List Comprehension Examples ===")

    # Example 1 — squares
    nums = [1, 2, 3, 4, 5]
    squares = [x * x for x in nums]
    print("Squares:", squares)

    # Example 2 — filter even numbers
    evens = [x for x in nums if x % 2 == 0]
    print("Evens:", evens)

    # Example 3 — transform strings
    words = ["python", "is", "fun"]
    upper_words = [w.upper() for w in words]
    print("Upper:", upper_words)

    # Example 4 — nested loop
    pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
    print("Pairs:", pairs)


if __name__ == "__main__":
    run()
