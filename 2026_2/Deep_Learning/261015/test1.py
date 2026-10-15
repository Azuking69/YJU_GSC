import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# ============================================================
# 1. 데이터 준비 — 07번과 동일 (Mine = 1, 60/20/20 분할, train 통계로 표준화)
# ============================================================
ds = fetch_openml("sonar", version=1, as_frame=True)
X = ds.data.to_numpy(dtype=float)
y = (ds.target == "Mine").astype(int).to_numpy()

X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, stratify=y, random_state=40, test_size=0.7
)

X_valid, X_test, y_valid, y_test = train_test_split(
    X_temp, y_temp, stratify=y_temp, random_state=40, test_size=0.5
)

N, D = X_train.shape


train_mean = X_train.mean(axis = 0)
train_std = X_train.std(axis=0)

X_train = (X_train - train_mean) / train_std
X_valid = (X_valid - train_mean) / train_std
X_test = (X_test - train_mean) / train_std



# ==========================Hyperparameters==================================
epochs = 1
lr = 0.1

# ==========================Parameters==================================
w = np.zeros(D)
b = 0.0

# ==========================Model==================================
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def predict(x, w, b):
    return sigmoid(x @ w + b)


# ===========================Optimizer================================
def gradient_step(w, b):
    """Gradient Descent 한 걸음"""
    H = predict(X_train, w, b)
    w -= lr * X_train.T @ (H - y_train) / N
    b -= lr * np.mean(H - y_train)
    return w, b

# ===========================================================



for epoch in range(epochs + 1):
    gradient_step(w, b)