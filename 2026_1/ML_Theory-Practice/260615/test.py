import numpy as np

bar = np.arange(12).reshape(3, 4)

print(f"bar\n{bar}\n")                   # shape(3, 4)
                                         # shape[1] -> 4
print(bar.shape[0], bar.shape[1])        # shape[0] -> 3

print(f"axis=1\n{bar.sum(axis=1)}\n")
print(f"axis=0\n{bar.sum(axis=0)}\n")
print(f"axis=1\n{bar.sum(axis=1)}\n")