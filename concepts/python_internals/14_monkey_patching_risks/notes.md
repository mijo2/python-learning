# Monkey Patching Risks in Python

## Overview
Monkey patching is the practice of dynamically modifying classes or modules at runtime. While powerful, it comes with significant risks.

## What is Monkey Patching?
- Changing module functions
- Adding methods to classes
- Modifying built-in types
- Patching third-party libraries

## Common Uses
- Testing (mocking)
- Hotfixes
- Extending libraries
- Debugging

## Risks and Problems
- **Hard to Debug**: Changes are invisible in code
- **Brittle**: Breaks with library updates
- **Unexpected Behavior**: Other code expects original behavior
- **Thread Safety**: Can cause race conditions
- **Maintenance**: Hard to track and maintain

## Examples of Risks
```python
# Patching a function
import some_module
original = some_module.func
some_module.func = lambda: "patched"

# Later, another part of code fails because it expects original behavior
```

## Safer Alternatives
- Use inheritance
- Composition
- Dependency injection
- Proper patching libraries (e.g., `unittest.mock`)

## Best Practices
- Avoid in production code
- Document patches clearly
- Use context managers for temporary patches
- Test thoroughly

## When It's Acceptable
- In tests with proper cleanup
- For development/debugging
- When no other options exist