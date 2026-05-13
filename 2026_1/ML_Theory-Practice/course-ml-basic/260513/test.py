import random

# Data
x_data = [i for i in range(1, 10)]
y_data = [0.7 * x + 0.2 for x in x_data]
number_of_sample = len(x_data)

# Hyperparameters
epochs = 300
batch_size = 3
lr = 0.01

# Model parameters
w = random.random()
b = random.random()

# Training
# Epoch loop
for epoch in range(1, epochs + 1):
    epoch_loss = 0.0
    # shuffring
    indices = list(range(number_of_sample))
    random.shuffle(indices)
    # print(f"indices: {indices}")

    # Batch loop
    for start_index in range(0, number_of_sample, batch_size):
        # print(f"R indices: \
        #   {indices[start_index:start_index \
        #   + batch_size]}")

        w_grad = 0.0
        b_grad = 0.0

        sample_idx = indices[start_index : start_index + batch_size]

        # Sample loop
        for index in sample_idx:
            x = x_data[index]
            y = y_data[index]

            # Prediction
            pred = w * x + b

            # Error
            error = pred - y

            # Gradient
            w_grad += 2 * x * error
            b_grad += 2 * error

            # loss
            epoch_loss += error**2

        # MSE
        w_grad /= len(sample_idx)
        b_grad /= len(sample_idx)

        # Parameter update
        w = w - lr * w_grad
        b = b - lr * b_grad

    if epoch % 10 == 0:
        print(f"EPOCH: {epoch}")
        print(f"Loss: {epoch_loss:.2f}")
        print(f"w: {w:.2f}, b: {b:.2f}")
