import numpy as np

pred = 0.0000_0000_0000_0000_1

bar = np.array([-1, 2, 3, np.inf, -np.inf])
# bar -> -inf, -1, 2, 3, inf

# np.clip(원데이터, 최소값, 최대값)
print(np.clip(bar, -10, 100))

eps = 1e-15 # log(0) 방지용 아주 작은 수
H_safe = np.clip(H, eps, 1 - eps)