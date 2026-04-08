import random

# 1. Data set
x_data = [count for count in range(1, 50 + 1)]
y_data = [0.3 * x + 1 for x in x_data]
num_of_sumple = len(x_data)


# 2. Parameter 초기화
w = random.random()
b = random.random()

# 3. Hyper Parameter 설정
epochs = 50
lr = 0.001

# 4. Model Learning
for i in range(num_of_sumple):
  # 
