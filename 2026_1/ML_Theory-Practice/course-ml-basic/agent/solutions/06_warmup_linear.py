"""정답: Linear Warmup (per-step)"""

import random

# ============================================================
# 데이터셋 (변경 금지) -- 정답: H(x) = 0.5x + 2
# ============================================================
random.seed(0)
x_data = [i for i in range(1, 21)]
y_data = [0.5 * x + 2 + random.uniform(-0.3, 0.3) for x in x_data]


# ============================================================
# 하이퍼파라미터 + 파라미터 초기화
# ============================================================
n = len(x_data)
epochs = 500
batch_size = 4
base_lr = 0.001
warmup_steps = 250  # 5 step/epoch × 50 epoch 분량
w, b = 0.0, 0.0

print(
    f"Linear Warmup (per-step) -- base_lr={base_lr}, epochs={epochs}, "
    f"batch_size={batch_size}, warmup_steps={warmup_steps}\n"
)


# ============================================================
# 학습 루프
# ============================================================
random.seed(42)
global_step = 0
for epoch in range(1, epochs + 1):
    # 매 epoch 데이터 셔플
    indices = list(range(n))
    random.shuffle(indices)

    loss_sum = 0.0
    n_batches = 0

    for start in range(0, n, batch_size):
        global_step += 1

        # ---- Linear Warmup: 0 → base_lr 선형 증가, 이후 base_lr 고정 ----
        #   step <= warmup_steps : lr = base_lr × (step / warmup_steps)
        #   step >  warmup_steps : (step / warmup_steps) > 1
        #                          → min(1.0, ..) 로 상한 clip → base_lr 고정
        lr = base_lr * min(1.0, global_step / warmup_steps)

        # ---- 배치 내 gradient + loss 누적 ----
        # MSE 미분: dw = (2/m) Σ error·x,  db = (2/m) Σ error  (error = pred - y)
        batch_indices = indices[start : start + batch_size]
        m = len(batch_indices)
        dw, db, batch_loss = 0.0, 0.0, 0.0
        for i in batch_indices:
            x, y = x_data[i], y_data[i]
            error = (w * x + b) - y
            dw += error * x
            db += error
            batch_loss += error**2

        dw = (2.0 / m) * dw
        db = (2.0 / m) * db

        # 파라미터 업데이트 (gradient descent)
        w -= lr * dw
        b -= lr * db

        loss_sum += batch_loss / m
        n_batches += 1

    if epoch == 1 or epoch % 100 == 0:
        print(
            f"Epoch {epoch:4d} | step {global_step:5d} | "
            f"lr: {lr:.5f} | Loss: {loss_sum / n_batches:.4f} | "
            f"w: {w:.2f}, b: {b:.2f}"
        )

print(f"\n최종 w = {w:.2f}, b = {b:.2f}  (정답 w=0.5, b=2.0)")
