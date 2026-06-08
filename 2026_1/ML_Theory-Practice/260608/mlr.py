import numpy as np

# MLR: Parameter -> 4 ea
w_true = np.array([0.2, 0.4, 0.5, 0.6]).reshape(-1, 1)
b_true = 2.0

# -4.0 ~ 4.0 -> (5, 4)
x_data = (np.random.random((5, 4)) - 0.5) * 8
y_data = x_data @ w_true + b_true

# parameter
epochs = 1
w = np.random.random((4, 11))
b = np.random.random()

for epoch in range(1, epochs + 1):
    y_pred = x_data @ w + b
    
    error = y_pred - y_data
    print(error)