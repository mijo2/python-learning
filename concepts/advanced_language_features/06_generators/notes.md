# Generators

**Generators** are functions that yield values lazily, producing items on demand. They use `yield` instead of `return`, creating iterators.

## Basic Generator

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(3):
    print(num)  # 1\n2\n3
```

## How They Work

- `yield` pauses the function, saving state.
- `next()` resumes from where it left off.
- When exhausted, raises `StopIteration`.

## Generator Expressions

Like list comprehensions but lazy.

```python
gen = (x**2 for x in range(5))
print(list(gen))  # [0, 1, 4, 9, 16]
```

## Benefits

- **Memory Efficient**: Generate large sequences without storing all.
- **Infinite Sequences**: Possible with generators.
- **Pipelines**: Chain generators.

## Advanced: send() and throw()

```python
def accumulator():
    total = 0
    while True:
        value = (yield total)
        if value is not None:
            total += value

gen = accumulator()
next(gen)  # Prime
print(gen.send(5))  # 5
print(gen.send(3))  # 8
```

## Best Practices

- Use for large data or streams.
- Avoid complex state in generators.
- Use `itertools` with generators.

Experiment with infinite generators. This leads to generator pipelines. Next, context managers.