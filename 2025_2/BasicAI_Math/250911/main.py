import numpy as np
import matplotlib.pyplot as plt

# 関数 y = -5x^2 + 20x
def height(x):
    return -5*x**2 + 20*x

# x の範囲（0秒～5秒）
x = np.linspace(0, 5, 200)
y = height(x)

# グラフ作成
plt.figure(figsize=(8,6))
plt.plot(x, y, label="y = -5x² + 20x", color="orange")

# 軸
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)

# 最高点 (x=2, y=20)
plt.scatter(2, 20, color="red")
plt.annotate("(2, 20)", (2, 20), xytext=(10, 10), textcoords="offset points", color="red")

# 落下点 (x=4, y=0)
plt.scatter(4, 0, color="blue")
plt.annotate("(4, 0)", (4, 0), xytext=(10, -20), textcoords="offset points", color="blue")

plt.title("the relationship between the height and the time of the ball")
plt.xlabel("time (seconds)")
plt.ylabel("height")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
