# Coroutines

**Coroutines** are generators that can receive values via `send()`, enabling two-way communication. They extend generators for cooperative multitasking.

## Basic Coroutine

```python
def coroutine():
    while True:
        received = (yield)
        print(f"Received: {received}")

c = coroutine()
next(c)  # Prime
c.send("Hello")  # Received: Hello
c.send("World")  # Received: World
```

## How They Work

- `yield` suspends and can receive values.
- `send(value)` resumes and passes value to `yield`.
- `throw()` raises exception in coroutine.
- `close()` terminates.

## Advanced: Producer-Consumer

```python
def consumer():
    total = 0
    while True:
        value = (yield total)
        if value is None:
            break
        total += value

c = consumer()
next(c)  # Prime
print(c.send(5))  # 5
print(c.send(3))  # 8
c.send(None)  # Close
```

## Uses

- Event loops (asyncio basis)
- Pipelines with feedback
- State machines

## Best Practices

- Prime with `next()` or `send(None)`.
- Handle exceptions with `try/except`.
- Use for async patterns pre-asyncio.

Experiment with a coroutine-based accumulator. This is the basis for async programming. Next, context managers.