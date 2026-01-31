# Coroutines Examples

def averager():
    total = 0
    count = 0
    average = 0
    while True:
        value = (yield average)
        if value is None:
            break
        total += value
        count += 1
        average = total / count

avg = averager()
next(avg)  # Prime
print(avg.send(5))  # 5.0
print(avg.send(10))  # 7.5
print(avg.send(15))  # 10.0
avg.send(None)

# Echo coroutine
def echo():
    try:
        while True:
            received = (yield)
            yield received
    except GeneratorExit:
        print("Exiting")

e = echo()
next(e)
print(e.send("Hi"))  # Hi
next(e)
print(e.send("Bye"))  # Bye
e.close()  # Exiting