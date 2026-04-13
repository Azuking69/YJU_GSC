import random

# 전체 흐름
# Dataset -> Model(H(x)=wx+b) -> Loss -> Optimizer

# 1.Dataset
x_data = [count for count in range(1, 51)]
y_data = [0.3 * x + 1 for x in x_data]
num = len(x_data)

# 2. 설정
# 2-1 Parameter(w, b) 초기화
w = random.random()
b = random.random()

# 2-2 HyperParameter 초기화
learning_rate = 0.001  # 한 번에 얼마나 이동할지 결정하는 값
epoch = 50

# 3. 학습 반복
# 3-1 epoch 횟수만큼 반복
for i in range(epoch):
    # 3-2 Gradient 초기화
    w_grad = 0.0
    b_grad = 0.0
    # 3-3 Loss값도 초기화
    loss = 0.0

    # 3-4 전체를 순회
    # Model: H(x) = wx + b
    for j in range(num):
        y = w * x_data[j] + b

        # 오차 계산
        # Error: 예측값 - 정답
        error = y - y_data[j]
        # loss = (y^ - y)**2
        loss += error**2

        # Gradient 계산
        # 미분을 사용해서 기울기를 구하기
        w_grad += 2 * x_data[j] * error
        b_grad += 2 * error

    # 3-5 평균을 구하기
    # Cost: Loss의 평균
    cost = loss / num

    # 3-6 방향 결정
    # Gradient / num
    w_grad = w_grad / num
    b_grad = b_grad / num

    # 3-7 Parameter update
    # 조금씩으로 update
    w = w - learning_rate * w_grad
    b = b - learning_rate * b_grad

    # 3-8 epoch마다 결과를 출력
    print(f"epoch: {i} | 손실: {cost} | w: {w} | b: {b}")

# 4. 최종 결과 출력
print(f"\nw: {w} | b: {b}")
