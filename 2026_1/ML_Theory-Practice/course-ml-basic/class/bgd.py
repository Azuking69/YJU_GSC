import random

# ============================================================
# 1. 데이터셋
#    정답: H(x) = 0.3x + 1  →  w=0.3, b=1
# ============================================================
# x_data = [ 1, 2, 3, 4, 5 ... 50]
# y_data = [ 1.3, 1.6, 1.9, 2.2, 2.5 ... 16.0]
x_data = [count for count in range(1, 51)]
y_data = [0.3 * x + 1 for x in x_data]
num_of_sample = len(x_data)


# 2. 파라미터 초기화 (w, b)
w = random.random()
b = random.random()

# 3. 하이퍼파라미터 설정 (learning_rate, epochs)
learning_rate = 0.001
epochs = 50

# 4. 학습 루프 (epoch 반복)
for i in range(epochs):
    # 4-1. 그래디언트 초기화
    grad_w = 0.0
    grad_b = 0.0
    loss = 0.0

    # 4-2. 전체 샘플 순회 (BGD: 모든 샘플을 다 본 뒤 업데이트)
    # (a) 예측값 계산: H(x) = wx + b
    for j in range(num_of_sample):
        y = w * x_data[j] + b

        # (b) 오차 계산: error = 예측값 - 실제값
        error = y - y_data[j]

        # (c) 그래디언트 누적: grad_w += 2 * x * error
        #                    grad_b += 2 * error
        grad_w += 2 * x_data[j] * error
        grad_b += 2 * error
        loss += error**2

    # 4-3. 평균 그래디언트 계산 (누적값 / n) Loss -> Cost
    grad_w = grad_w / num_of_sample
    grad_b = grad_b / num_of_sample
    loss = loss / num_of_sample

    # 4-4. 파라미터 업데이트: w = w - lr * grad_w
    lr = learning_rate
    w = w - lr * grad_w
    b = b - lr * grad_b

    # 4-5. 손실(loss) 출력 (학습 경과 확인)
    print(f"epoch: {i + 1} | 손실(loss): {loss} | w: {w:.4f}, b{b:4f}")

# 5. 최종 결과 출력
print(f"\nw: {w}, b: {b}")
