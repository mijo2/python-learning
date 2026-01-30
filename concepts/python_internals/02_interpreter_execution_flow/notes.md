# Interpreter Execution Flow

After understanding bytecode, let's explore how Python's interpreter executes it. The **execution flow** involves compiling source to bytecode, then running it in the PVM (Python Virtual Machine) with the GIL managing threads.

## Compilation Phase

1. **Source Code** → **AST (Abstract Syntax Tree)** via `ast` module.
2. **AST** → **Bytecode** via `compile()`.
3. **Bytecode** stored in `.pyc` files.

```python
import ast
code = "x = 1 + 2"
tree = ast.parse(code)
print(ast.dump(tree))  # Shows AST structure
```

## Execution Phase

- **PVM**: Interprets bytecode instruction by instruction.
- **Stack-Based**: Uses evaluation stack for operations.
- **Frames**: Each function call creates a frame (local namespace).

```python
import dis

def func():
    x = 1
    return x + 2

dis.dis(func)
# Shows LOAD_CONST, STORE_FAST, etc.
```

## Key Components

- **Code Objects**: Compiled bytecode with constants, names, etc.
- **Global Interpreter Lock (GIL)**: Ensures thread safety.
- **Import System**: Loads modules dynamically.

## Execution Steps

1. Load module.
2. Execute top-level code.
3. On function call: Create frame, push to call stack.
4. Execute bytecode in frame.
5. Return result, pop frame.

Debug with `pdb` or `sys.settrace()`. This flow explains performance and debugging. Next, CPython vs PyPy.