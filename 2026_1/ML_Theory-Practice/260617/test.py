import numpy as np

np.random.seed(0)
N, D = 5, 4

w_true = np.array([0.2, 0.4, 0.5, 0.7]).reshape(-1, 1) # D, 1
b_true = 2.0 

x_data = (np.random.random((N, D)) - 0.5) * 8 #N, D
y_data = x_data @ w_true + b_true # N, 1

# Model Parameters
w = np.random.random((D, 1)) # D, 1
b = np.random.random()

# Hyper Parameters
epochs = 1000
lr = 0.007

#Loop: Training, BGD
for epochs in range(1, epochs + 1):
    # prediction
    y_pred = x_data @ w + b # N, 1
    
    print(y_pred)
    ...
      
# print(f"w_true: {w_true}\n")
# print(f"b_true: {b_true}\n")
# print("*" * 10)
# print(f"w: {w}\n")
# print(f"b: {b}\n")