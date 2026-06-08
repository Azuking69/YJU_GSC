import numpy as np

# MLR: Parameter -> 4 ea
w_true = np.array([0.2, 0.4, 0.5, 0.6]).reshape(-1, 1)
b_true = 2.0

# -4.0 ~ 4.0 -> (5, 4)
x_data = (np.random.random((5, 4)) - 0.5) * 8
y_data = x_data @ w_true + b_true

print(x_data)
print()
print(w_true)
print()
print(y_data)
