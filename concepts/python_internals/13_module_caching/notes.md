# Module Caching in Python

## Overview
Python caches imported modules in `sys.modules` to avoid reloading them. This improves performance but can cause issues during development.

## How Caching Works
- First import: Module loaded, executed, stored in `sys.modules`
- Subsequent imports: Return cached module from `sys.modules`
- Key is module name (e.g., 'mymodule')

## Benefits
- Faster imports
- Ensures single instance of module
- Prevents re-execution of module code

## Issues
- Changes to module file not reflected until reload
- Memory usage for large modules
- Testing complications

## Managing Cache
```python
import sys
import importlib

# Remove from cache
if 'mymodule' in sys.modules:
    del sys.modules['mymodule']

# Reload
import mymodule
importlib.reload(mymodule)
```

## Cache Keys
- For packages: 'package.submodule'
- For `__main__`: Special case
- Built-in modules: Also cached

## When Cache is Bypassed
- Using different import paths
- Module not found in cache
- Explicit reload

## Best Practices
- Use `importlib.reload()` in development
- Be careful with mutable module globals
- Use version control for module changes