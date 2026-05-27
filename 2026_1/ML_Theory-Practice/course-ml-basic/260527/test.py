import numpy as np

# 2 x 1 x 3
bar = np.array([[[3, 4, 20]], [[1, 2, 30]]])


print(type(bar))
print(bar.ndim)
print(bar.shape)
print(bar.shape[0], bar.shape[1], bar.shape[2])
