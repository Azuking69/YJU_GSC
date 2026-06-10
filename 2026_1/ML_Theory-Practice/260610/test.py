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
epochs = 1

#Loop: Training
for epoch in range(1, epochs + 1):
    # Prediction
    y_pred = x_data @ w + b # N, 1
    
    print(x_data)
    print(w)
    print(b)
    
    print(y_pred)
    
    # Error: Prediction - Y
    error = y_pred - y_data
    
    # Loss
    
    # Grad
    
    # Update