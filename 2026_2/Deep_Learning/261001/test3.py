import numpy as np


bar16 = np.array([1, 2], dtype = np.float16)
bar32 = np.array([1, 2], dtype = np.float32)
bar64 = np.array([1, 2], dtype = np.float64)

print(np.finfo(bar16.dtype).eps)
print(np.finfo(bar32.dtype).eps)
print(np.finfo(bar64.dtype).eps)
