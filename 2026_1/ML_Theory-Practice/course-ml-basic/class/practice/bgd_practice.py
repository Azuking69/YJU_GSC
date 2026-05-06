import random

# 전체 흐름
# Dataset -> Model(H(x)=wx+b) -> Loss -> Optimaizer

# 1. Dataset
x_data = [count for count in range(1, 51)]
y_data = [0.03 * x + 1 for x in x_data]
num = len(x_data)

# 2. Setting
# 2-1 Parameter(w, b) 초기화
w = random.random()
b = random.random()

# 2-2 Hyperparameter 초기화
learning_rate = 0.001  # 얼마나 이동할 지
epoch = 50

# 3. 학습 반복
# 3-1 epoch의 횟수만큼 반복
for i in range(epoch):
    # 3-2 Gradient 초기화
    w_grad = 0.0
    b_grad = 0.0
    loss = 0.0

    # 3-3 Dataset를 Model에 들어가기
    # Model: H(x) = wx + b
    for j in range(num):
        y = w * x_data[j] + b

        # 3-4 오차 계산
        # error: 예측값 - 정답
        error = y - y_data[j]
        # loss: (예측값 - 정답) ** 2
        loss += error**2

        # Gradient 계산
        # 미분을 사용해서 기울기를 구하기
        w_grad += 2 * x_data[j] * error
        b_grad += 2 * error

    # 3-5 평균을 계산
    # Cost: loss / num
    cost = loss / num

    # 3-6 방향 결정
    # Gradient / num
    w_grad = w_grad / num
    b_grad = b_grad / num

    # 3-7 Parameter 업데이트
    w = w - learning_rate * w_grad
    b = b - learning_rate * b_grad

    # 3-8 epoch마다 결과를 출력
    print(f"epoch: {i + 1} | 손실: {cost} | w: {w} | b: {b}")

# 4. 최종 결과
print(f"\nw: {w} | b: {b}")
