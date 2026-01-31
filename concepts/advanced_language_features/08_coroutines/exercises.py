# Coroutines Exercises

# Exercise: Create a coroutine that collects strings and returns concatenated

def string_collector():
    collected = []
    while True:
        s = (yield)
        if s is None:
            break
        collected.append(s)
    return "".join(collected)

# Uncomment to test
# c = string_collector()
# next(c)
# c.send("Hello")
# c.send(" ")
# c.send("World")
# try:
#     c.send(None)
# except StopIteration as e:
#     print(e.value)  # Hello World