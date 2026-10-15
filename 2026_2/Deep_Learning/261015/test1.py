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

print(X.shape)
print(y.shape)