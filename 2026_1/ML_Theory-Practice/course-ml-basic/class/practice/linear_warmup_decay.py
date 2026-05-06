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
# Hyper parameter setting
epochs = 500
batch_size = 4
base_lr = 0.008

# 전체 step 수 계산
total_steps = epochs * (data_size // batch_size)

# 전체 step의 절반은 warmup
warmup_steps = total_steps // 2
# 나머지 절반은 decay
decay_steps = total_steps - warmup_steps

# parameter setting
w = 0.0
b = 0.0

# global_step : 1 부터 시작
global_step = 1


# Loop: epoch
for epoch_i in range(1, epochs + 1):
    # 매 epoch마다 데이터 순서 섞기
    random_data = list(range(data_size))
    random.shuffle(random_data)

    # epoch loss 초기화
    epoch_loss = 0.0

    # Loop: batch(step)
    for batch_i in range(0, data_size, batch_size):
        # batch단위로 index를 가져오기
        batch_index = random_data[batch_i : batch_i + batch_size]

        # batch마다 gradient, loss를 초기화
        w_grad = 0.0
        b_grad = 0.0
        batch_loss = 0.0

        # Loop: sample
        for sample_i in batch_index:
            # data 가져오기
            x = x_data[sample_i]
            y = y_data[sample_i]

            # 예측값 계산
            # Model: H(X) = wx + b
            y_pred = w * x + b

            # error: 예측값 - 정답값
            error = y_pred - y

            # parameter 기울기 값 계산 누적
            w_grad += 2 * x * error
            b_grad += 2 * error

            # batch loss 누적
            batch_loss += error**2

        # batch 평균
        batch_len = len(batch_index)
        w_grad = w_grad / batch_len
        b_grad = b_grad / batch_len
        batch_loss = batch_loss / batch_len

        # Warmup: 0 → base_lr 선형 증가
        if global_step < warmup_steps:
            lr = base_lr * (global_step / warmup_steps)

        # Linear Decay: base_lr → 0 선형 감소
        else:
            lr = base_lr * max(0.0, 1 - (global_step - warmup_steps) / decay_steps)

        # parameter update
        w = w - lr * w_grad
        b = b - lr * b_grad

        # epoch loss 누적
        epoch_loss += batch_loss * batch_len

        # 매 batch 마다 +1
        global_step += 1

    # epoch loss 평균
    epoch_loss = epoch_loss / data_size

    # loss 출력
    if epoch_i == 1 or epoch_i % 100 == 0:
        print(f"Epoch: {epoch_i} | Loss: {epoch_loss:.4f} | w: {w:.4f} | b: {b:.4f}")

# 최종 결과 출력
print(f"\nFinal Loss: {epoch_loss:.4f} | Final w: {w:.4f} | Final b: {b:.4f}")
