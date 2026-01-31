# Advanced Comprehensions

## Overview
Comprehensions provide a concise way to create collections from iterables. Beyond basic list comprehensions, Python supports advanced patterns including nested comprehensions, dictionary/set comprehensions, and conditional logic.

## Types of Comprehensions
- **List Comprehensions**: `[expr for item in iterable]`
- **Dictionary Comprehensions**: `{key: value for item in iterable}`
- **Set Comprehensions**: `{expr for item in iterable}`
- **Generator Expressions**: `(expr for item in iterable)`

## Advanced Patterns
```python
# Nested comprehensions
matrix = [[i*j for j in range(3)] for i in range(4)]

# Conditional comprehensions
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# Multiple conditions
filtered = [x for x in data if condition1 and condition2]

# Nested loops
pairs = [(x, y) for x in range(3) for y in range(3) if x != y]
```

## Dictionary Comprehensions
```python
# Basic
squares = {x: x**2 for x in range(5)}

# With conditions
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}

# Key transformation
upper_names = {name.upper(): age for name, age in data.items()}
```

## Set Comprehensions
```python
# Remove duplicates
unique_lengths = {len(word) for word in words}

# Complex expressions
squares_set = {x**2 for x in range(-5, 6)}
```

## Generator Expressions
```python
# Memory efficient
sum_squares = sum(x**2 for x in range(1000000))

# Chaining
processed = (process(item) for item in data if condition(item))
```

## Performance Considerations
- **Memory Usage**: Lists vs generators
- **Readability**: Complex comprehensions can be hard to read
- **Debugging**: Harder than explicit loops
- **Optimization**: Comprehension overhead

## Best Practices
- Use for simple transformations
- Avoid deeply nested comprehensions
- Consider readability over conciseness
- Use generator expressions for large data
- Profile performance when needed

## Common Pitfalls
- **Variable Leakage**: Loop variables persist
- **Complex Logic**: Better as regular loops
- **Memory Issues**: Large list comprehensions
- **Side Effects**: Avoid in comprehensions
