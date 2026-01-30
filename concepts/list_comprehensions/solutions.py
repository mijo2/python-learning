def solutions():
    nums = list(range(1, 11))
    print([x*x for x in nums])

    nums = list(range(1, 31))
    print([x for x in nums if x % 3 == 0])

    words = ["Python", "APPLE", "sky", "COMPUTER", "AI"]
    print([w.lower() for w in words if len(w) > 4])

    print([(n, n*n) for n in range(1, 9)])

    matrix = [[1,2,3],[4,5],[6,7,8]]
    print([x for row in matrix for x in row])

    nums = [3, -1, 5, -9, 2]
    print([x if x >= 0 else 0 for x in nums])

    print([(x, y) for x in range(1,5) for y in range(1,5) if x != y])

    sentence = "List comprehensions are powerful"
    print([len(w) for w in sentence.split()])


if __name__ == "__main__":
    solutions()
