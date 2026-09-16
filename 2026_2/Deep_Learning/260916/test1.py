from sklearn.datasets import load_breast_cancer
import numpy as np

X, y = load_breast_cancer(return_X_y=True)

# print(ds.SESCR)
# print(f"X: {X.shape}, y: {y.shape}")
print(X[0, :5])
print(y[0])
print(np.count_nonzero(y))