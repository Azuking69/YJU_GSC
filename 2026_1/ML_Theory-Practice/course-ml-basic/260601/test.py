import numpy as np

bar = np.arange(1, 17)
pos = bar.reshape(4, 4)
foo = pos.reshape(2, 4, 2)
print(f"bar: {bar}")
print("*" * 20)
print(f"pos: {pos}")
print("*" * 20)
print(f"foo: {foo}")
