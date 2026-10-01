import numpy as np


bar = np.array([1, 2, 3])
foo = np.array([1.0, 2, 3.0])
pos = np.array([1.0, 2.0, 3.0], dtype=np.float32)

print(bar.dtype) # int32
print(foo.dtype) # float64
print(pos.dtype) # float32