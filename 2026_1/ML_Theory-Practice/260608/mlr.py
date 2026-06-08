import numpy as np

# MLR: Parameter -> 4 ea
w_true = np.array([0.2, 0.4, 0.5, 0.6]).reshape(-1, 1)
b_true = 2.0

# -4.0 ~ 4.0 -> (5, 4)
# x_dara = (np.random.random((5, 4)) - 0.5) * 8 

bar = np.arange(1, 10).reshape(-1, 3)
foo = np.array([0.1, 0.2, 0.3, 0.4])

print(bar)
print(foo)
print(bar + 2)