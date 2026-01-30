# Interpreter Execution Flow Exercises Solutions

import ast

expr = "a + b * c"
tree = ast.parse(expr)
print(ast.dump(tree))