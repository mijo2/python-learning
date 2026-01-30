# Bytecode Model Examples

import dis

def add(a, b):
    return a + b

print("Bytecode for add function:")
dis.dis(add)

def loop_example():
    for i in range(3):
        print(i)

print("\nBytecode for loop_example function:")
dis.dis(loop_example)

# You can also disassemble modules or code objects
code = compile("x = 1 + 2", "<string>", "exec")
print("\nBytecode for compiled expression:")
dis.dis(code)