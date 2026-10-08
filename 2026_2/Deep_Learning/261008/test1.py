from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support

np.random.seed(0)

X, y = datasets.load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, train_size=0.7, random_state=40, stratify=y)

N = len(X_train)
D = len(X_train[0])

mu = X_train.mean(axis = 0) # (D, )
sigma = X_train.std(axis = 0) # (D, )

X_train = (X_train - mu) / sigma
X_test = (X_test - mu) / sigma



# Hyper-parameters
epochs = 1000
lr = 0.1

# Model : Logistic regression
w = np.random.randn(D) # (D, )
b = np.random.randn() # (b, )

def lg_logit(w:np.ndarray, b:float, x:np.ndarray)->np.ndarray:
    # x @ w + b
    return x @ w + b

def sigmoid(z:np.ndarray)->np.ndarray:
    # 1 / (1 + np.exp(-z))
    return 1 / (1 + np.exp(-z))

def lg_predict(w:np.ndarray, b:np.float64, x:np.ndarray)->np.ndarray:
    logit = lg_logit(w, b, x)
    return sigmoid(logit)



for epoch in range(1, epochs + 1):
    pred = lg_predict(w, b, X_train)

    # error
    error = pred - y_train # (N,)

    # w_grad, b_grad
    w_grad = error @ X_train / N # (D, )
    b_grad = error.mean() # (1,) S

    # update
    w = w - lr * w_grad
    b = b - lr * b_grad

    # loss
    # EPS -> np.clip
    if epoch % 100 == 0:
        loss = -np.mean(y_train * np.log(pred) + (1-y_train)*np.log(1-pred))
        print(f"epoch: {epoch}, train loss: {loss:.4f}")



print(type(b))