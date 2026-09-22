from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np

X, y = datasets.load_breast_cancer(return_X_y=True)

X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.7, random_state=40, stratify=y)

N = len(X_train)
D = len(X_train[0])

print(N, D)