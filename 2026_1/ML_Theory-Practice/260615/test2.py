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

#Loop: Training
for epoch in range(1, epochs + 1):
    # Prediction
    y_pred = x_data @ w + b    # N, 1
    
    # Error: Prediction - Y
    error = y_pred - y_data    # n, 1
    
    # Grad
    w_grad = (2 / N) * x_data.T @ error # N, 1
    b_grad = (2 / N) * error.sum()      # 1

    # Update
    w = w - lr * w_grad # D, 1
    b = b - lr * b_grad # 1
    
    # Loss
    if epoch % 100 == 0:
      print(f"Loss: {(error ** 2).mean():.4f}\n")
      
print(f"w_true: {w_true}\n")
print(f"w: {w.T}\n")
print(f"b_true: {b_true}\n")
print(f"b: {b.T}\n")