import numpy as np

bar = np.array([3])  # list, tuple
#                                        ndim, shape
# 3                                  ->   0,   ()
# [1, 2, 3]                          ->   1,   (3,)
# [[1, 2], [3, 4]]                   ->   2,   (2, 3)
# [[1, 2], [3, 4]], [[1, 2], [3, 4]] ->   3,   (2, 2, 2)

print(type(bar)) # <class 'numpy.ndarray'>
print(bar.ndim) # 次元数
print(bar.shape) # 形
