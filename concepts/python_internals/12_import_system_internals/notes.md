# Import System Internals

## Overview
Python's import system is responsible for loading and managing modules. Understanding its internals helps with debugging import issues and creating dynamic imports.

## Key Components
- `sys.modules`: Cache of loaded modules
- `sys.path`: List of directories to search for modules
- `importlib`: Standard library for import operations
- `__import__()`: Built-in function for importing

## Import Process
1. Check `sys.modules` for already loaded module
2. Find module file using `sys.path`
3. Execute module code
4. Add to `sys.modules`
5. Return module object

## Import Variants
- `import module`
- `from module import name`
- `import module as alias`
- `from module import *`

## Dynamic Imports
```python
import importlib
mod = importlib.import_module('mymodule')
```

## Reloading Modules
```python
import importlib
import mymodule
importlib.reload(mymodule)
```

## Custom Importers
- Implement `importlib.abc.MetaPathFinder`
- `sys.meta_path` list
- For custom loading logic

## Common Issues
- Circular imports
- Module not found
- Stale cached modules