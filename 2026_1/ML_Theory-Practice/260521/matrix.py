import numpy as np

samples = np.arange(1, 17).reshape(4, 4)
W = np.array([0.1, 0.2, 0.3, 0.4]).reshape(-1)

print(samples)
print(W)

print(samples @ W)
