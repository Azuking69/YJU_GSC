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
batch_size = 4
base_lr = 0.008

# 전체 step 수 계산
total_steps = epochs * (data_size // batch_size)

# 전체 step의 절반은 warmup
warmup_steps = total_steps // 2

# decay
decay_steps = total_steps - warmup_steps

# Parameter setting
w = 0.0
b = 0.0

# global step: 1부터 시작
global_step = 1

# Loop: epoch
for loop_epoch in range(1, epochs + 1):
    # epoch마다 데이터 순서 섞기
    random_data = list(range(data_size))
    random.shuffle(random_data)

    # epoch loss 초기화
    epoch_loss = 0.0


    # Loop: batch(step)
    for loop_batch in range(0, data_size, batch_size):
        # batch단위로 index를 가져오기
        batch_index = random_data[loop_batch:loop_batch + batch_size]

        # batch마다 gradient, loss를 초기화
        grad_w = 0.0
        grad_b = 0.0
        loss = 0.0


        # Loop sample
        for loop_sample in batch_index:
            # data 가져오기
            x = x_data[loop_sample]
            y = y_data[loop_sample]

            # 예측값 계산
            # Model: H(X) = wx + b
            pred_y = w * x + b

            # error: 예측값 - 정답
            error = pred_y - y

            # Parameter 기울기 누적
            grad_w += 2 * x * error
            grad_b += 2 * error
            loss += error ** 2

        
        # batch 평균 계산
        batch_len = len(batch_index)
        grad_w = grad_w / batch_len
        grad_b = grad_b / batch_len
        loss = loss / batch_len

        # Warmup: 0 -> base_lr 선형 증가
        if global_step < warmup_steps:
            lr = base_lr * (global_step / warmup_steps)
        
        # Decay: base_lr -> 0 선형 감소
        else:
            lr = base_lr * max(0.0, 1 - (global_step - warmup_steps) / decay_steps)
        
        # Parameter update
        w = w - lr * grad_w
        b = b - lr * grad_b

        # epoch loss 누적
        epoch_loss += loss * batch_len

        # batch마다 + 1
        global_step += 1


    # epoch loss 평균
    epoch_loss = epoch_loss / data_size

    # loss 출력
    if loop_epoch == 1 or loop_epoch % 100 == 0:
        print(f"Epoch: {loop_epoch} | Loss: {epoch_loss:.4f} | w: {w:.4f} | b: {b:.4f}")

# 최종 결과 출력
print(f"\nFinal Loss: {epoch_loss:.4f} | Final w: {w:.4f} | Final b: {b:.4f} | Final global steps: {global_step}")