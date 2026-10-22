import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# ============================================================================
# 1. 데이터 준비 — 07번과 동일 (Mine = 1, 60/20/20 분할, train 통계로 표준화)
# ============================================================================
ds = fetch_openml("sonar", version=1, as_frame=True)
X = ds.data.to_numpy(dtype=float)
y = (ds.target == "Mine").astype(int).to_numpy()

# train_test_split을 두 번 사용하여 train, valid, test 데이터셋을 나눈다.
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, stratify=y, random_state=40, test_size=0.7
)

# train_test_split을 두 번 사용하여 train, valid, test 데이터셋을 나눈다.
X_valid, X_test, y_valid, y_test = train_test_split(
    X_temp, y_temp, stratify=y_temp, random_state=40, test_size=0.5
)

# N: train
# D: feature
N, D = X_train.shape

# train_mean: train 데이터의 평균
# train_std: train 데이터의 표준편차
train_mean = X_train.mean(axis = 0)
train_std = X_train.std(axis=0)

# train 데이터를 표준화한다.
X_train = (X_train - train_mean) / train_std
# valid 데이터를 표준화한다.
X_valid = (X_valid - train_mean) / train_std
# test 데이터를 표준화한다.
X_test = (X_test - train_mean) / train_std



# ==========================Hyperparameters====================================
epochs = 150
lr = 0.1

patience = 50
best_val_loss = np.inf
best_epoch = 0
best_w, best_b = None, None
checkpoints = [10, 30, 50, 100, 150, 300, 1000, 3000, 10_000]

# ==========================Parameters=========================================
w = np.zeros(D)
b = 0.0

# ==========================Model==============================================
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def predict(x, w, b):
    return sigmoid(x @ w + b)

# =========================Loss================================================
def bce_loss(H, y, eps=1e-15):
    H = np.clip(H, eps, 1 - eps)                # log(0) 방지
    return -np.mean(y * np.log(H) + (1 - y) * np.log(1 - H))

# ===========================Optimizer=========================================
def gradient_step(w, b):
    """Gradient Descent 한 걸음"""
    H = predict(X_train, w, b)
    w -= lr * X_train.T @ (H - y_train) / N
    b -= lr * np.mean(H - y_train)
    return w, b

# =============================================================================

for epoch in range(1, epochs + 1):
    w, b = gradient_step(w, b)

    val_loss = bce_loss(predict(X_valid, w, b), y_valid)

    if val_loss < best_val_loss:
        best_val_loss = val_loss
        best_epoch = epoch
        best_w, best_b = w.copy(), b             # 복사본을 저장한다. w 는 이후에도 계속 갱신된다
    elif epoch - best_epoch >= patience:
        print(f"   [early stopping] epoch {epoch}: {patience} epoch 동안 개선 없음 → 중단")
        break

    if epoch in checkpoints:
            print_row(epoch, w, b)


target_names = ["ROCK(0)", "MINE(1)"]

def evaluate(title, w, b):
    H_test = predict(X_test, w, b)
    y_pred = (H_test >= 0.5).astype(int)
    print(f"\n[{title}]  test loss: {bce_loss(H_test, y_test):.4f}")
    print(classification_report(y_test, y_pred, target_names=target_names, digits=4))

evaluate(f"Early stopping — epoch {best_epoch} 의 w", best_w, best_b)
evaluate(f"끝까지 학습 — epoch {epochs} 의 w", w, b)