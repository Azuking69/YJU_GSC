import numpy as np

pred = 0.000_0000_0000_0000_1
y = 0

# Logistic regression
loss = -y * np.log(pred) - (1 - y) * np.log(1 - pred)
print(loss)