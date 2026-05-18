import random
import math

# ============================================================
# 1. 데이터셋
#    정답: H(x) = 0.3x + 0.1  →  w=0.3, b=0.1
# ============================================================
# Data
num_samples = 50
x_data = [i for i in range(1, num_samples + 1)]
y_data = [0.3 * x + 1 for x in x_data]

# Hyperparameters
epochs = 500
base_lr = 0.01
batch_size = 5
enable_shffling = True
global_step = 0
warmup_ratio = 0.4


# Derive parameters
total_step = math.ceil(num_samples / batch_size) * epochs
warmup_step = math.ceil(total_step * warmup_ratio)

# Model parameters
w = random.random()
b = random.random()

# Model training
# Loop: epoch
for epoch in range(1, epochs + 1):
    epoch_loss = 0.0
    # Shuffling
    if enable_shffling:
        sample_index = list(range(num_samples))
        random.shuffle(sample_index)
        # print(f"Shuffled indices: {sample_index}")

        # Loop step
        for batch_index in range(0, num_samples, batch_size):
            w_grad = 0.0
            b_grad = 0.0
            global_step += 1

            if global_step <= warmup_step:
                lr = base_lr * min(1.0, global_step / warmup_step)
            else:
                lr = base_lr * min(
                    0.0, (global_step - warmup_step) / (total_step - warmup_step)
                )

            batch_indies = sample_index[batch_index : batch_index + batch_size]
            # print(batch_indies)
            # print(f"Batch index: {batch_index}, end: {batch_index + batch_size}")

            # Loop: sample
            for idx in batch_indies:
                num_batch_samples = len(batch_indies)
                x = x_data[idx]
                y = y_data[idx]

                # Prediction
                y_pred = w * x + b

                # Error
                error = y_pred - y

                # Loss
                epoch_loss += error**2

                # Gradient
                w1_grad = 2 * x * error
                b_grad = 2 * error

            # Gradient avg
            w_grad /= num_batch_samples
            b_grad /= num_batch_samples

            # Parameter update
            w = w - lr * w_grad
            b = b - lr * b_grad

    if epoch % 100 == 0:
        print(
            f"Epoch: {epoch}\nLoss: {epoch_loss / num_samples:.2f}\nw: {w:.2f}, b: {b:.2f}"
        )
