import torch

# 1️⃣ 中身が未初期化のTensor
x = torch.empty(5, 3)
print("1. empty(未初期化)")
print(x, "\n")

# 2️⃣ 乱数で初期化
x = torch.rand(5, 3)
print("2. rand(乱数初期化)")
print(x, "\n")

# 3️⃣ ゼロで初期化
x = torch.zeros(5, 3, dtype=torch.long)
print("3. zeros(ゼロ初期化)")
print(x, "\n")

# 4️⃣ 直接指定
x = torch.tensor([5.5, 3])
print("4. tensor(直接指定)")
print(x, "\n")

# 5️⃣ 既存Tensorから新しいTensor
x = x.new_ones(5, 3, dtype=torch.double)   # 元xを参考に新しい行列
print("5-1. new_ones(既存から新しいTensor)")
print(x, "\n")

x = torch.randn_like(x, dtype=torch.float) # 同じ形で乱数、型をfloatに
print("5-2. randn_like(同じ形で乱数)")
print(x, "\n")

# 📏 Tensorのサイズ
print("6. size(形の確認)")
print(x.size(), "\n")

# 🛠 Tensorの操作例
y = torch.rand(5, 3)
print("7-1. 加算（演算子）")
print(x + y, "\n")

print("7-2. 加算（関数形式）")
print(torch.add(x, y), "\n")

# 結果を指定先に保存
result = torch.empty(5, 3)
torch.add(x, y, out=result)
print("7-3. 結果を指定先に保存")
print(result, "\n")

# インプレース処理
y.add_(x)
print("7-4. インプレース処理（yを書き換え）")
print(y, "\n")

# 🔎 インデックス・スライス
print("8. インデックス・スライス（2列目）")
print(x[:, 1], "\n")

# 🔄 形を変える（reshape）
x = torch.randn(4, 4)
y = x.view(16)       # フラット化
z = x.view(-1, 8)    # 2行8列に変換
print("9. 形の変換")
print("x:", x.size(), " y:", y.size(), " z:", z.size(), "\n")

# 🎯 要素を取り出す
x = torch.randn(1)
print("10. 要素を取り出す")
print("Tensor:", x)
print("Python数値:", x.item())