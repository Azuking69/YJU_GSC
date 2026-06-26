import numpy as np

np.random.seed(0)
N, D = 5, 4

w_true = np.array([0.2, 0.4, 0.5, 0.7]).reshape(-1, 1) # D, 1
b_true = 2.0 

x_data = (np.random.random((N, D)) - 0.5) * 70 #N, D
x_data = (x_data - x_data.mean(0)) / x_data.std(0)
y_data = x_data @ w_true + b_true # N, 1

# Model Parameters
w = np.random.random((D, 1)) # D, 1
b = np.random.random()

# Hyper Parameters
epochs = 50_000
lr = 0.003

#Loop: Training, BGD
for epoch in range(1, epochs + 1):
    # prediction
    y_pred = x_data @ w + b # N, 1
    
    # error
    error = y_pred - y_data
    
    # grad: w_grad, b_grad
    w_grad = (2 / N) * x_data.T @ error #D, 1
    b_grad = (2 / N) * error.sum() # 1
    
    # update parameters
    w = w - lr * w_grad
    b = b - lr * b_grad
    
    if epoch % 1000 == 0:
      print(f"epoch: {epoch}, Loss: {(error**2).mean():.4f}\n")
    ...
      
print(f"w_true: {w_true}\n")
print(f"b_true: {b_true}\n")
print("*" * 50)
print(f"w: {w}\n")
print(f"b: {b}\n")