import numpy as np

X_Data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)
Y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1])

N = len(Y)
D = X_Data.shape[-1]

epochs = 1
lr = 0.01

w = np.random.randn()
b = np.random.randn()

# Leraning loop
for epoch in range(1, epochs + 1):
    # Prediction : 1) logit[wx + b] -> 2) sigmoid(1/1 + e^-z) -> H
    z = w * X_Data + b
    H = 1 / (1 + np.exp(-z))

    # Error : H - y
    error = H - Y

    # Calculate gradient : w, b
    # w_grad = error * x / N
    # b_grad = error / N
    w_grad = np.dot(error.T, X_Data) / N
    b_grad = np.sum(error) / N

    # Update parameters
    # w = w - lr * w_grad
    # b = b - lr * b_grad
    w -= lr * w_grad
    b -= lr * b_grad

    # Loss : -y*logH - (1-y)log(1-H)
    loss = -np.mean(Y * np.log(H) + (1 - Y) * np.log(1 - H))


    print(f"{epoch} th: Epoch\n w: {w} b: {b}")