import numpy as np

# x_data
x_data = np.arange(1, 26).reshape(5, 5)

# 샘플이 랜덤......
x_data = (np.random.random(12) - 0.5).reshape(3, 4) * 4  # -0.5 ~ 0.5

print(x_data)
