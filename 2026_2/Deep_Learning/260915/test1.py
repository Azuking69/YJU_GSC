import numpy as np

X_Data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)
Y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1])

N = len(Y)
D = X_Data.shape[-1]

epochs = 10000
lr = 0.1

w = np.random.randn(D)
b = np.random.randn()

# Leraning loop
for epoch in range(1, epochs + 1):
    # Prediction : 1) logit[wx + b] -> 2) sigmoid(1/1 + e^-z) -> H
    logit = X_Data @ w + b # (N, )
    predict = 1 / (1 + np.exp(-logit)) # (N, )
    print(f"logit: {logit}")
    print(f"predict: {predict}")

    # Error : H - y
    error = predict - Y

    # Calculate gradient : w, b
    # w_grad = error * x / N
    # b_grad = error / N
    w_grad = error @ X_Data / N
    b_grad = np.mean(error)
    print(f"w_grad: {w_grad} b_grad: {b_grad}")

    # Update parameters
    # w = w - lr * w_grad
    # b = b - lr * b_grad
    w -= lr * w_grad
    b -= lr * b_grad

    # Loss : -y*logH - (1-y)log(1-H)
    if epoch % 1000 == 0:
        loss = -np.mean(Y*np.log(predict) + (1 - Y) * np.log(1 - predict))
        print(f"{epoch} th, loss: {loss}")

y = 1 / (1 + np.exp(-2 * w + b))
print((y >= 0.5).astype(bool))