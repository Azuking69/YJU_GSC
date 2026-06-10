import numpy as np

np.random.seed(0)
N, D = 5, 4

# w_true = np.array([0.2, 0.4, 0.5, 0.7]).reshape(-1, 1) # (4, )
w_true = np.array([0.2, 0.4, 0.5, 0.7]).reshape(-1, 1) # D, 1
b_true = 2.0 

x_data = (np.random.random((N, D)) - 0.5) * 8
print(x_data)