import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

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
epochs = 10
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

    print(logit[:1, ])
    print(logit.shape)
    # print(logit.max(), logit.min())

    # predict: 1 / (1 + exp^ - z)
    pred = 1 / (1 + np.exp(-logit)) 
    print(pred[:1, ])
    print(pred.shape)

    # error

    # w_grad, b_grad

    # update

    print(f"epoch: {epoch}")