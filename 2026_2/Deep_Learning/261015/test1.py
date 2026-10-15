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


print(f"X: {X.shape}")
print(f"X_train: {X_train.shape}")
print(f"X_valid: {X_valid.shape}")
print(f"X_test: {X_test.shape}")