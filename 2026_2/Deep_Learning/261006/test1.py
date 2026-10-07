import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support

X, y = load_breast_cancer(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42)

print(X_train.shape, X_test.shape)

N = len(X_train)
D = len(X_train[0])
print(N, D)

print(f"before: {X_train}")
mu = X_train.mean(axis=0)
sigma = X_train.std(axis=0)

sigma = np.where(sigma == 0, 1.0, sigma)


# 검증 세트를 별도로 만들었다면 같은 기준 적용
# X_val = (X_val - mu) / sigma
X_train = (X_train - mu) / sigma
X_test = (X_test - mu) / sigma
print(f"after: {X_train[0]}")


# Hyperparameters
epochs = 100
lr = 0.1


# Model: Logistic Regression
w = np.random.randn(D)
b = np.random.randn()

print("max")
print(X_train[0].max())


for epoch in range(1, epochs + 1):
    # logit: WX + b
    logit: np.ndarray
    logit = X_train @ w + b

    # predict: 1 / (1 + exp^ - z)
    pred = 1 / (1 + np.exp(-logit)) 

    # error
    error = pred - y_train

    # w_grad, b_grad
    w_grad =  error @ X_train / N # (D, )
    b_grad = error.mean() / N # (1, )

    # update
    w = w - lr * w_grad
    b = b - lr * b_grad

    # loss
    # ESP -> np.clip
    if epoch % 10 == 0:
        loss = -np.mean(y_train * np.log(pred + (1 - y_train) * np.log(1 - pred))
        print(f"epoch: {epoch}, train loss: {loss:.4f}")

t_logit = X_test @ w + b
t_pred = 1 / (1 + np.exp(-t_logit))
t_pred (t_pred >= 0.5).astype(int)

accuracy = (t_pred == y_test).mean()

print(f"accuracy: {accuracy}")
print(confusion_matrix(y_test, t_pred))
print(classification_recall_fscore_support(y_test, t_pred))