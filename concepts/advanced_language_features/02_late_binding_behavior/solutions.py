# Late Binding Behavior Exercises Solutions

funcs = [lambda x=i: x for i in range(3)]
print([f() for f in funcs])  # [0, 1, 2]