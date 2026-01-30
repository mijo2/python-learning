# Interpreter Execution Flow Examples

import ast
import dis

# AST parsing
code = "x = 1 + 2"
tree = ast.parse(code)
print("AST:", ast.dump(tree, indent=2))

# Disassemble
def func():
    x = 1
    return x + 2

print("Bytecode:")
dis.dis(func)