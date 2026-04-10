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
for i in range(epochs):
    # 그라디엔트 초기화
    grad_w = 0.0
    grad_b = 0.0
    loss = 0.0

    # sample 순회
    for j in range(num_of_sumple):
        # Model H(x) = wx + b
        y = w * x_data[j] + b

        # Error 계산
        error = y - y_data[j]

    # 누적
    grad_w += 2 * x_data[j] * error
    grad_b += 2 * error
    loss = error**2

    # parameter update
    w = w - lr * grad_w
    b = b - lr * grad_b

    # 이번 epoch의 결과 확인
    print(f"epoch: {i + 1} | loss: {loss} | w: {w:.4} | b: {b:.4}")

# 최종 결과
print(f"\nw: {w} | b: {b}")
