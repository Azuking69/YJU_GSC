from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support

np.random.seed(0)

X, y = datasets.load_breast_cancer(return_X_y=True)
X_train, X_T, y_train, y_T = \
    train_test_split(X, y, train_size=0.7, random_state=40, stratify=y)

X_valid, X_test, y_valid, y_test = \
    train_test_split(X_T, y_T, train_size=0.5, random_state=40, stratify=y_T)

print(y_train.shape)
print(y_valid.shape)
print(y_test.shape)

# N = len(X_train)
# D = len(X_train[0])

# mu = X_train.mean(axis = 0) # (D, )
# sigma = X_train.std(axis = 0) # (D, )

X_train = (X_train - mu) / sigma
X_test = (X_test - mu) / sigma



# Hyper-parameters
epochs = 10000
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

def lg_predict(w:np.ndarray, b:float, x:np.ndarray)->np.ndarray:
    logit = lg_logit(w, b, x)
    return sigmoid(logit)

def loss_bce(w:np.ndarray, b:float, x:np.ndarray, y:np.ndarray, title:str|None = None):
    pred = lg_predict(w, b, x)
    EPS = np.finfo(pred.dtype).eps
    pred = np.clip(pred, EPS, 1 - EPS)
    loss = -np.mean(y * np.log(pred) + (1-y)*np.log(1-pred))
    print(f"\t{title} loss: {loss:.4f}", end="")



for epoch in range(1, epochs + 1):
    pred_train = lg_predict(w, b, X_train)

    # error
    error = pred_train - y_train # (N,)

    # w_grad, b_grad
    w_grad = error @ X_train / N # (D, )
    b_grad = error.mean() # (1,) S

    # update
    w = w - lr * w_grad
    b = b - lr * b_grad

    # loss
    # EPS -> np.clip
    if epoch % 1000 == 0:
        print(f"epoch: {epoch}", end="")
        # Loss: train dataset
        loss_bce(w, b, X_train, y_train, "train")
        # Loss: valid dataset
        loss_bce(w, b, X_test, y_test, "valid")
        print()