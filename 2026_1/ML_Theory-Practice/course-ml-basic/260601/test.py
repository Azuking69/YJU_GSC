import numpy as np

# x_data
x_data = np.arange(1, 26).reshape(5, 5)

# indexing
# Python - slice indexing
# start:stop:step
# start, stop 생략 시 -> 전체
# stop 생략 시 -> 끝
# step 생략 시 -> +1
print(x_data[::1, ::])
print(x_data[1:-1, 1:-1])
