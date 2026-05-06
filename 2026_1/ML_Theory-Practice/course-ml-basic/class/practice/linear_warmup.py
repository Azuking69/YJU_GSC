import random

# ============================================================
# 데이터셋 (변경 금지) -- 정답: H(x) = 0.5x + 2  (w=0.5, b=2)
# ============================================================
random.seed(0)
x_data = [i for i in range(1, 21)]
y_data = [0.5 * x + 2 + random.uniform(-0.3, 0.3) for x in x_data]
data_size = len(x_data)


# ============================================================
# 학생 구현 영역
# ============================================================
# Hyperparameter setting
epochs = 500
batch = 4
base_lr = 0.001
warmup_steps = 250

# Parameter setting
w = 0.0
b = 0.0

# global_step : 1 부터 시작
global_step = 1

# loop: epoch
# 1 epoch당 step 수 = data_size / batch = 20 / 4 = 5
for i in range(1, epochs + 1):
    # 매 epoch마다 데이터 순서 섞기
    random_data = list(range(data_size))
    random.shuffle(random_data)

    # epoch loss 초기화
    epoch_loss = 0.0

    # loop: batch(step)
    for j in range(0, data_size, batch):
        # batch단위로 index를 가져오기
        batch_index = random_data[j : j + batch]

        # batch마다 gradient, loss를 초기화
        w_grad = 0.0
        b_grad = 0.0
        loss = 0.0

        # loop: sample
        # 예측값 계산
        # 에러 계산
        for k in batch_index:
            x = x_data[k]
            y = y_data[k]

            # 예측값을 계산
            # Model: H(X) = wx + b
            pred_y = w * x + b

            # error: 예측값 - 정답값
            error = pred_y - y

            # 파라메터 기울기 값 계선 누적
            w_grad += 2 * x * error
            b_grad += 2 * error

            # 로스값 계산 후 누적
            loss += error**2

        # 평균 계산
        # 마지막 배치는 크기가 다를 수 있음
        batch_len = len(batch_index)
        w_grad = w_grad / batch_len
        b_grad = b_grad / batch_len
        loss = loss / batch_len

        # warmup
        # warmup_steps = 250 → 250 / 5 = 50 epoch 동안 warmup 진행
        lr = base_lr * min(1.0, global_step / warmup_steps)

        # Parameter update
        w = w - lr * w_grad
        b = b - lr * b_grad

        # epoch loss 누적
        epoch_loss += loss * batch_len

        # 매 batch 마다 +1
        global_step += 1

    # epoch loss 평균
    epoch_loss = epoch_loss / data_size

    # 로스 출력
    if i == 1 or i % 100 == 0:
        print(f"Epoch: {i} | Loss: {epoch_loss:.4f} | w: {w:.4f} | b: {b:.4f}")

# 최종 결과 출력
print(
    f"\nFinal Loss: {epoch_loss:.4f}\nFinal w: {w:.4f}\nFinal b: {b:.4f}\nFinal global_step: {global_step}"
)
