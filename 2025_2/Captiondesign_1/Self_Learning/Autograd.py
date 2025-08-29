import torch

# requires_gradをONにしたTensor
x = torch.ones(2, 2, requires_grad=True)
print(x)

# 計算すると履歴が残る
y = x + 2
print(y)
print(y.grad_fn)

# 複雑な計算も追跡される
z = y * y * 3
out = z.mean()
print(z, out)

# 勾配を計算する
out.backward()
print(x.grad)