# Closures

Welcome to advanced language features! Closures are a powerful concept that lets functions "remember" variables from their surrounding scope, even after that scope has ended. Think of it as a function carrying its own backpack of data.

## What is a Closure?

A closure occurs when an inner function references variables from its outer (enclosing) function, and the outer function returns the inner one. The inner function "closes over" those variables.

```python
def outer(x):
    def inner(y):
        return x + y  # x is from outer scope
    return inner

add_five = outer(5)
print(add_five(3))  # 8 (remembers x=5)
```

The `inner` function is a closure—it captures `x` from `outer`.

## Why Closures Matter

1. **Data Encapsulation**: Hide state without classes.
2. **Function Factories**: Create customized functions.
3. **Callbacks**: Useful in event-driven code.
4. **Memory Efficiency**: Avoid global variables.

Closures enable functional programming patterns in Python.

## Key Points

- **Free Variables**: Variables captured from enclosing scope.
- **Cell Objects**: Internally, Python uses cells to store captured variables.
- **Late Binding**: Changes to closed-over variables affect the closure.

```python
def make_multiplier(factor):
    return lambda x: x * factor  # Closure

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))  # 10
print(triple(5))  # 15
```

## Pitfalls

- **Mutable Defaults**: Avoid modifying closed-over mutables unexpectedly.
- **Late Binding Gotcha**: Loops can cause issues if not careful.

Experiment with closures to build custom counters or validators!