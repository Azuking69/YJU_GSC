from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np

X, y = datasets.load_breast_cancer(return_X_y=True)

X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.7, random_state=40, stratify=y)

N = len(X_train)
D = len(X_train[0])

print(N, D)

# Hyperparameters
epochs = 20
lr = 0.1

# Model: Logistic Regression
w = np.random.randn(D)
b = np.random.randn()


for epoch in range(1, epochs + 1):
    # logit: WX + b
    logit: np.ndarray
    logit = X_train @ w + b

    print(logit.shape)
    print(logit.max(), logit.min())


    # predict: 1 / (1 + exp^ - z)
    pred = 1 / (1 + np.exp(-logit)) 

    # error

    # w_grad, b_grad

    # update

    print(f"epoch: {epoch}")