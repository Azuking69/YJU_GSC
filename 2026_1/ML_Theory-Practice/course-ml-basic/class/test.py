# ============================================================
# 1. 데이터셋
#    정답: H(x) = 0.5x + 2  →  w=0.5, b=2
# ============================================================
import random

# Dateset
x_data = [1, 2, 3, 4]
# x_data = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
y_data = [2.5, 3.0, 3.5, 4.0]

num_of_samples = len(x_data)

epochs = 1000
learning_rate = 0.01

w = random.random()
b = random.random()

# epoch만큼 학습
for epoch in range(1, epochs + 1):
    # print(f"{epoch}번째 epoch")

    w_grad = 0.0
    b_grad = 0.0
    loss = 0.0

    # sample을 순회
    for x, y in zip(x_data, y_data):
        # 예축값 계산
        # H(x) = wx + b
        predict = w * x + b

        # Error 계산
        error = predict - y

        # w의 기울기(Loss) 값 누적
        w_grad += 2 * x * error
        # b의 기울기(Loss) 값 누적
        b_grad += 2 * x * error

        # loss 값 누젹
        loss += error**2

    w_grad /= num_of_samples
    b_grad /= num_of_samples
    loss /= num_of_samples

    # update parameters
    w = w - learning_rate * w_grad
    b = b - learning_rate * b_grad

    if epoch % 100 == 0:
        print(f"epoch: {epoch}, loss: {loss:.4f}")

# 정답: H(x) = 0.5x + 2  →  w=0.5, b=2
print(f"x: {x}, y: {y}")
